import aioredis

from app.core.config import Config

redis = aioredis.from_url(Config.REDIS_URL)
