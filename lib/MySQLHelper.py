#coding=utf-8

import pymysql
from configs import config
from lib.log import logger
class MySQLHelper(object):

    def __init__(self, dbName):
        if dbName == "panacube":
            self.conn = config.panacube
        if dbName == "panastor":
            self.conn = config.panastor


    """查询返回只有一条结果"""
    def get_one(self, sql, params):
        conn = pymysql.connect(**self.conn)    #打开数据库连接
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)    #使用cursor方法获取操作游标
        try:
            logger.info('the sql is : %s' % sql)
            logger.info('the params is : %s' % str(params))
            cur.execute(sql, params)   # 使用execute方法执行sql语句
            data = cur.fetchone()      # 使用fetchone方法获取一条数据
            logger.info('the result data is :%s' % data)
            return data
        except:
            print("Error: unable to fetch data")
        finally:
            cur.close()                # 关闭cursor
            conn.close()               # 关闭数据库连接


    def get_many(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            logger.info('the sql is :%s' % sql)
            logger.info('the params is : %s' % str(params))
            cur.execute(sql, params)
            data = cur.fetchall()      # 使用fetchall方法获取全部数据
            logger.info('the result data is :%s' % str(data))
            return data
        except Exception as e:
            print("Error: unable to fetch data")
        finally:
            cur.close()
            conn.close()


    def insert_one(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor()
        try:
            logger.info('the sql is :%s' % sql)
            logger.info('the params is : %s' % str(params))
            cur.execute(sql, params)
            conn.commit()
            return u'插入数据库成功'
        except Exception as e:
            conn.rollback()  #回滚事务
        finally:
            cur.close()
            conn.close()


    def insert_many(self, sql, params):
        conn = pymysql.connect(**self.conn)
        logger.info('the sql is :%s' % sql)
        try:
            logger.info('the params is : %s' % str(params))
            cur = conn.cursor()
            cur.executemany(sql, params)
            conn.commit()
            return u'批量插入数据库成功'
        except Exception as e:
            conn.rollback()
        finally:
            cur.close()
            conn.close()


    def update_one(self,sql,params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            logger.info('the sql is :%s' % sql)
            logger.info('the params is : %s' % str(params))
            ret = cur.execute(sql, params)
            conn.commit()        #提交到数据库执行
            return u'更新数据库成功'
        except Exception as e:
            conn.rollback()
        finally:
            cur.close()
            conn.close()


    def update_oneLine (self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            logger.info('the sql is :%s' % sql)
            logger.info('the params is : %s' % str(params))
            ret = cur.execute(sql, params)
            conn.commit()
            return ret
        except Exception as e:
            conn.rollback()
        finally:
            cur.close()
            conn.close()


    def delete_one(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            logger.info('the sql is :%s' % sql)
            logger.info('the params is : %s' % str(params))
            ret = cur.execute(sql, params)
            conn.commit()
            return u'删除数据库成功'
        except Exception as e:
            conn.rollback()
        finally:
            cur.close()
            conn.close()

