# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time
import logging

import grpc

import ShowLibInterface_pb2
import ShowLibInterface_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

import Manager
import sqlite3
class Greeter(ShowLibInterface_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.manger = Manager.ShowLibManager()
    def InsertRCHashRecord(self, request, context):
        record = []
        record.append(request.hash)
        record.append(request.name)
        record.append(int(request.size,10))
        record.append(request.mtime)
        self.manger.AddRecordToRCHashTable(record)
        return ShowLibInterface_pb2.Result(RET = 0)
    #批量插入数据
    def InsertRCHashRecords (self, request_iterator, context):
        conn = sqlite3.connect("ShowLib.db")
        for res in request_iterator:
            logging.info(res)
            record = []
            record.append(res.hash)
            record.append(res.name)
            record.append(int(res.size,10))
            record.append(res.mtime)
            logging.info(record)
            self.manger.AddRecordToRCHashTableNeedConn(record,conn)
            ret = ShowLibInterface_pb2.Result(RET = 0)
            yield ret
        conn.close()
    #获取RCHash记录数
    def GetRCHashCount (self, request, context):
        count = self.manger.ShowRecordCount()
        return ShowLibInterface_pb2.RecordCount(Count = count)
    #获取RCHash记录
    def GetRCHashRecords (self, request, context): 
        for record in self.manger.GetRecordList():
            yield ShowLibInterface_pb2.RCHashRecord(hash = record[0],
                name = record[1],
                size = str(record[2]),
                mtime = record[3]
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ShowLibInterface_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='server.log', level=logging.INFO, format=LOG_FORMAT)

if __name__ == '__main__':
    logging.basicConfig()
    serve()
