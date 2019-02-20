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
class Greeter(ShowLibInterface_pb2_grpc.GreeterServicer):

    def InsertRCHashRecord(self, request, context):
        record = []
        record.append(request.hash)
        record.append(request.name)
        record.append(request.size)
        record.append(request.mtime)
        Manager.AddRecordToRCHashTable(record)
        return ShowLibInterface_pb2.Result(RET = 0)


def serve():
    Manager.CreateDB()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ShowLibInterface_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()