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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import ShowLibInterface_pb2
import ShowLibInterface_pb2_grpc

import FinderInterface
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='clinet.log', level=logging.INFO, format=LOG_FORMAT)
class ShowLibClient:
    def __init__(self,ConnectStr):
        self.channel = grpc.insecure_channel(ConnectStr)
        self.stub = ShowLibInterface_pb2_grpc.GreeterStub(self.channel)
    def __del__(self):
        self.channel.close()
    def GenerateRCHashRecord(self):
        for item in FinderInterface.GetAllRecords():
            yield ShowLibInterface_pb2.RCHashRecord(hash = item[1],name =item[0],size = str(item[2]),mtime = item[3])

    def InsertRCHashRecords(self):
        iter = self.GenerateRCHashRecord()
        print(iter)
        for res in self.stub.InsertRCHashRecords(iter):
            logging.info("Greeter client received: " + str(res.RET))

        ##for response in res
            #
    def InsertRCHashRecord(self):
        pass
    def GetRCHashCount(self):
        response = self.stub.GetRCHashCount(ShowLibInterface_pb2.Result(RET = 1))
        logging.debug("Greeter client received : RCHashCount =" + str(response.Count))
        return response.Count
    def GetRCHashRecords(self):
        response = self.stub.GetRCHashCount(ShowLibInterface_pb2.Result(RET = 1))
        logging.debug("Greeter client received: " + str(response.Count))

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ShowLibInterface_pb2_grpc.GreeterStub(channel)
        rclist = FinderInterface.ListvedioRC()
        for item in rclist:
            response = stub.InsertRCHashRecord(ShowLibInterface_pb2.RCHashRecord(hash = item[1],name =item[0],size = str(item[2]),mtime = item[3]))
            logging.debug("Greeter client received: " + str(response.RET))

if __name__ == '__main__':
    logging.basicConfig(filename='clinet.log')
    run()
