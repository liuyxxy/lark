#!/opt/cadadmin/users/anaconda3/bin/python
import pydotlib as dotlib
lib=dotlib.PLYPair()
lib.set_lexer(dotlib.create_lexer())
lib.set_parser(dotlib.create_parser())

print("Testing ...")
lib.parse_file('s22dpllsys500_ana_core_lib_ff_ff_0p63lv_1p66hv_125c_rcmax_fs_tpl_PVT005irdrpAULP.lib')
#lib.parse_file('s22sramull_16384x32m16b8_hd_rvt_ff_xx_0p77lv_0p88lv_0c_rcmin_tpnl_PVT.lib')
print(dir(lib))
print(lib.result)
