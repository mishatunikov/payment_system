from dataclasses import dataclass

from environs import Env


@dataclass
class DjangoSettings:
    debug: bool
    secret_key: str
    db_prod: bool


@dataclass
class Database:
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: str


@dataclass
class Config:
    django: DjangoSettings
    db: Database


def load_config() -> Config:
    env = Env()
    env.read_env()
    return Config(
        django=DjangoSettings(
            debug=env.bool('DEBUG'),
            secret_key=env.str('SECRET_KEY'),
            db_prod=env.bool('DB_PROD'),
        ),
        db=Database(
            MYSQL_DATABASE=env.str('MYSQL_DATABASE', 'payment_db'),
            MYSQL_USER=env.str('MYSQL_USER', 'payment_user'),
            MYSQL_PASSWORD=env.str('MYSQL_PASSWORD', 'payment_password'),
            MYSQL_HOST=env.str('MYSQL_HOST', '127.0.0.1'),
            MYSQL_PORT=env.str('MYSQL_PORT', '3306'),
        ),
    )


config: Config = load_config()
