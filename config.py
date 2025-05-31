from dataclasses import dataclass

from environs import Env


@dataclass
class DjangoSettings:
    debug: bool
    secret_key: str


@dataclass
class Config:
    django: DjangoSettings


def load_config() -> Config:
    env = Env()
    env.read_env()
    return Config(
        django=DjangoSettings(
            debug=env.bool('DEBUG'), secret_key=env.str('SECRET_KEY')
        ),
    )


config: Config = load_config()
