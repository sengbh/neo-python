
from neo.IO.Mixins import SerializableMixin
from neo.IO.BinaryWriter import BinaryWriter
from neo.IO.MemoryStream import MemoryStream
import ctypes


class StateBase(SerializableMixin):

    StateVersion= 0


    def Size(self):
        return ctypes.sizeof(ctypes.c_byte)


    @staticmethod
    def DeserializeFromDB(buffer):
        pass

    def Deserialize(self, reader):
        sv = reader.ReadByte()
        if sv != self.StateVersion:
            raise Exception("Incorrect State format")

    def Serialize(self, writer):
        writer.WriteByte(self.StateVersion)


    def ToByteArray(self):
        ms = MemoryStream()
        writer = BinaryWriter(ms)
        self.Serialize(writer)
        return ms.ToArray()