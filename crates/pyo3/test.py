from ast_grep_pyo3 import SgRoot

sg = SgRoot('let a = 123', 'javascript')
root = sg.root()

node = root.find(rule=dict(pattern = 'let $A = $B'), language = 'javascript')
assert node is not None
node = root.find(rule=dict(pattern = 'let $A = 456'), language = 'javascript')
assert node is None