from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from testcontainers.postgres import PostgresContainer

from db_services.engine_factory import EngineFactory
from db_services.db_service import post_to_postgres

from tests.edu_power_access_control import Base as Access_Control_Base, ACCESS_CONTROL_PREPARE_ROWS
from tests.edu_power_global import Base as Global_Base, GLOBAL_PREPARE_ROWS
from tests.edu_power_kc import Base as KC_Base, KC_PREPARE_ROWS
from .edu_power_group import Base as Group_Base, GROUP_PREPARE_ROWS


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestBases(metaclass=MetaSingleton):
    db = None
    main_url = None

    def __init__(self, db_image_name):
        __engine = EngineFactory()
        __engine.stand = 'localhost'
        # Создание контейнера из образа DB_IMAGE
        __postgres_container = PostgresContainer(image=db_image_name)
        self.db = __postgres_container.start()
        self.main_url = self.db.get_connection_url()

        __BASES = {'edu_power_access_control': {'class': Access_Control_Base, 'rows': ACCESS_CONTROL_PREPARE_ROWS},
                   'edu_power_kc': {'class': KC_Base, 'rows': KC_PREPARE_ROWS},
                   'edu_power_global': {'class': Global_Base, 'rows': GLOBAL_PREPARE_ROWS},
                   'edu_power_group': {'class': Group_Base, 'rows': GROUP_PREPARE_ROWS}
                   }

        # Создание баз, схем, наполнение данными
        for __base_name, __base_data in __BASES.items():
            self.create_base(base_name=__base_name)
            __engine.user, __engine.passw = 'test', 'test'
            __url = __engine.get_postgres_url(base_name=__base_name)
            self.create_schema(schema_name=__base_name, url=__url)
            __db_engine = __engine.get_engine(__base_name)
            __base_data.get('class').metadata.create_all(__db_engine)

            for __cls, __rows in __base_data.get('rows').items():
                __db_engine.execute(insert(__cls).values(__rows))

        #Создание процедуры change_sber_id_creds в БД edu_power_kc
        self.__create_procedures()


    def create_base(self, base_name):
        __engine = create_engine(self.main_url)
        __connection = __engine.connect()
        __connection.execution_options(isolation_level='AUTOCOMMIT').execute(f'create database {base_name}')
        __host, __port = self.main_url.replace('postgresql+psycopg2://test:test@', '').replace('/test', '').split(':')
        __new_base_url = f'postgresql+psycopg2://test:test@{__host}:{__port}/{base_name}'
        __engine = EngineFactory()
        __engine.add_local_db(base_name=base_name, url=__new_base_url)

    def create_schema(self, url, schema_name):
        __engine = create_engine(url)
        __connection = __engine.connect()
        __connection.execution_options(isolation_level='AUTOCOMMIT').execute(f'create schema {schema_name}')
        __connection.execution_options(isolation_level='AUTOCOMMIT').execute(f'create extension if not exists "uuid-ossp"')

    def __create_procedures(self):
        __base_name = 'edu_power_kc'
        __schema_name = 'edu_power_kc'
        sql = ''' create procedure change_sber_id_creds(realmname character varying, sberididpalias character varying, keyprovidername character varying, sberidtokenurlnew text, sberiduserinfourlnew text, sberidauthorizationurlnew text, clientidnew text, clientsecretnew text, privatekeynew text, certnew text)
                    language plpgsql
                as $$
                DECLARE
                    _internal_id VARCHAR(36);
                    _component_id VARCHAR(36);
                BEGIN
                    --изменение параметров idp
                
                
                    --обновление параметров idp(пример для секретного ключа)
                    -- указать корректный provider_alias
                    SELECT internal_id
                    INTO _internal_id
                    FROM identity_provider
                    --название idp
                    WHERE provider_alias= sberIdIdpAlias AND realm_id=realmName; --'sberidift'
                
                    UPDATE identity_provider_config
                    --в бд значчения никак не шифруются
                    SET value=clientSecretNew
                    --возможные значения для name можно получить из запроса - SELECT DISTINCT name FROM identity_provider_config
                    --clientSecret clientId
                    WHERE name='clientSecret' AND identity_provider_id=_internal_id;
                
                    UPDATE identity_provider_config
                        --в бд значчения никак не шифруются
                    SET value=clientIdNew
                        --возможные значения для name можно получить из запроса - SELECT DISTINCT name FROM identity_provider_config
                        --clientSecret clientId
                    WHERE name='clientId' AND identity_provider_id=_internal_id;
                
                    UPDATE identity_provider_config
                        --в бд значчения никак не шифруются
                    SET value=sberIdtokenUrlNew
                        --возможные значения для name можно получить из запроса - SELECT DISTINCT name FROM identity_provider_config
                        --clientSecret clientId
                    WHERE name='tokenUrl' AND identity_provider_id=_internal_id;
                
                    UPDATE identity_provider_config
                        --в бд значчения никак не шифруются
                    SET value=sberIdAuthorizationUrlNew
                        --возможные значения для name можно получить из запроса - SELECT DISTINCT name FROM identity_provider_config
                        --clientSecret clientId
                    WHERE name='authorizationUrl' AND identity_provider_id=_internal_id;
                
                    UPDATE identity_provider_config
                        --в бд значчения никак не шифруются
                    SET value=sberIdUserInfoUrlNew
                        --возможные значения для name можно получить из запроса - SELECT DISTINCT name FROM identity_provider_config
                        --clientSecret clientId
                    WHERE name='userInfoUrl' AND identity_provider_id=_internal_id;
                
                    -------------------------
                    --изменение параметров провайдера ключей
                
                    SELECT id
                    INTO _component_id
                    FROM component
                    WHERE realm_id=realmName
                            AND provider_id='rsa'
                            AND provider_type='org.keycloak.keys.KeyProvider'
                        --название провайдера ключей
                            AND name=keyProviderName; --'rsa-test'
                
                    UPDATE component_config
                    -- приватный ключ(или сервтификат) без обрамляющих строк
                    SET value=privateKeyNew
                    --возможные значения параметра name - SELECT DISTINCT name FROM component_config
                    --privateKey certificate
                    WHERE name='privateKey' AND component_id=_component_id;
                
                    UPDATE component_config
                        -- приватный ключ(или сервтификат) без обрамляющих строк
                    SET value=certNew
                        --возможные значения параметра name - SELECT DISTINCT name FROM component_config
                        --privateKey certificate
                    WHERE name='certificate' AND component_id=_component_id;
                
                END;
                $$; '''

        _ = post_to_postgres(sql=sql, db_name=__base_name, schema_name=__schema_name)
