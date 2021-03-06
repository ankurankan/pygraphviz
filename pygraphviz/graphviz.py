# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _graphviz
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


agopen = _graphviz.agopen
def agraphnew(name,strict=False,directed=False):
    if strict:
       if directed:
            return _graphviz.agopen(name,cvar.Agstrictdirected,None)
       else:
            return _graphviz.agopen(name,cvar.Agstrictundirected,None)
    else:
        if directed:
            return _graphviz.agopen(name,cvar.Agdirected,None)
        else:		 
            return _graphviz.agopen(name,cvar.Agundirected,None)

agclose = _graphviz.agclose
agread = _graphviz.agread
agwrite = _graphviz.agwrite
agisundirected = _graphviz.agisundirected
agisdirected = _graphviz.agisdirected
agisstrict = _graphviz.agisstrict
agnode = _graphviz.agnode
agidnode = _graphviz.agidnode
agsubnode = _graphviz.agsubnode
agfstnode = _graphviz.agfstnode
agnxtnode = _graphviz.agnxtnode
aglstnode = _graphviz.aglstnode
agprvnode = _graphviz.agprvnode
agedge = _graphviz.agedge
agidedge = _graphviz.agidedge
agsubedge = _graphviz.agsubedge
agfstin = _graphviz.agfstin
agnxtin = _graphviz.agnxtin
agfstout = _graphviz.agfstout
agnxtout = _graphviz.agnxtout
agfstedge = _graphviz.agfstedge
agnxtedge = _graphviz.agnxtedge
aghead = _graphviz.aghead
agtail = _graphviz.agtail
agattr = _graphviz.agattr
agattrsym = _graphviz.agattrsym
agnxtattr = _graphviz.agnxtattr
agget = _graphviz.agget
agxget = _graphviz.agxget
agset = _graphviz.agset
agxset = _graphviz.agxset
agsafeset = _graphviz.agsafeset
agattrname = _graphviz.agattrname
agattrdefval = _graphviz.agattrdefval
agsafeset_label = _graphviz.agsafeset_label
agattr_label = _graphviz.agattr_label
agsubg = _graphviz.agsubg
agfstsubg = _graphviz.agfstsubg
agnxtsubg = _graphviz.agnxtsubg
agparent = _graphviz.agparent
agroot = _graphviz.agroot
agdelsubg = _graphviz.agdelsubg
agnnodes = _graphviz.agnnodes
agnedges = _graphviz.agnedges
agdegree = _graphviz.agdegree
agraphof = _graphviz.agraphof
agnameof = _graphviz.agnameof
agdelnode = _graphviz.agdelnode
agdeledge = _graphviz.agdeledge
def agnameof(handle):
  name=_graphviz.agnameof(handle)
  if name is None:
     return None
  if name=='' or name.startswith('%'):
    return None
  else:
    return name 

AGRAPH = _graphviz.AGRAPH
AGNODE = _graphviz.AGNODE
AGOUTEDGE = _graphviz.AGOUTEDGE
AGINEDGE = _graphviz.AGINEDGE
AGEDGE = _graphviz.AGEDGE

cvar = _graphviz.cvar
Agdirected = cvar.Agdirected
Agstrictdirected = cvar.Agstrictdirected
Agundirected = cvar.Agundirected
Agstrictundirected = cvar.Agstrictundirected

