from kaitaistruct import KaitaiStream
from core.save.potionomics_save import PotionomicsSave
from core import resources

with open("samples/SaveSlot9", 'rb') as f:
    save = PotionomicsSave(KaitaiStream(f))
