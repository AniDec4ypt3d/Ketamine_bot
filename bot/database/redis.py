import redis
antidb = redis.Redis(host='reids', port=, password='', decode_responses = True)
# redis_connector = redis.Redis(host=REDIS_URI, port=REDIS_PORT, password= REDIS_PASS if REDIS_PASS else None, db=0, decode_responses=False)
# redis_session = RedisSession('mills', redis_connector)
