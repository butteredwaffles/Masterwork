from kaitaistruct import KaitaiStream
# from core.save.potionomics_save_slot import PotionomicsSave
# from core import resources
#
# with open("samples/SaveSlot9", 'rb') as f:
#     save = PotionomicsSave(KaitaiStream(f))

from core.save import potionomics_save
from parser import ue_save_parser

sample = ue_save_parser._load_from_json('core/save/test2.json')
sample_save = ue_save_parser.PotionomicsUESaveParser('core/save/test3.json')
pass