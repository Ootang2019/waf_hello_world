def options(opt):
    opt.load('compiler_cxx')

def configure(cnf):
    cnf.load('compiler_cxx')
    print("configure!")


def build(bld):
    bld(features='c cxx cxxprogram', source='hello_world.cpp', target='app')
    print("build!")
