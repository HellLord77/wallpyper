import ast
import contextlib
import json
import time
import tracemalloc


@contextlib.contextmanager
def timeit():
    start = time.time()
    yield
    print(time.time() - start)


def bench():
    tracemalloc.start()
    with timeit():
        # noinspection PyUnresolvedReferences
        from libs import ctyped  # < 0.8s -> 0.5s -> 0.3s
    print(tracemalloc.get_tracemalloc_memory() / (1024 * 1024), 'MB')
    tracemalloc.stop()


def get_type(node):
    if isinstance(node, ast.Attribute):
        return f'{node.value.id[1:]}.{node.attr}'
    elif isinstance(node, ast.Name):
        return f'interface.{node.id}'


def _get_interfaces(tree: ast.Module | ast.ClassDef):
    interfaces = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            bases = tuple(ast.unparse(base) for base in node.bases)
            if bases or node.name.startswith('_'):
                # print(node.name)
                # print(bases)
                funcs = {}
                for node_body in node.body:
                    if isinstance(node_body, ast.AnnAssign):
                        annot = node_body.annotation
                        if isinstance(annot, ast.Subscript):
                            args, res = annot.slice.elts
                            funcs[ast.unparse(node_body.target)] = [ast.unparse(elt) for elt in args.elts], ast.unparse(res)
                        else:
                            funcs[ast.unparse(node_body.target)] = None
                # pprint.pprint(funcs)
                interfaces[node.name] = [bases, funcs]
            else:
                interfaces[node.name] = _get_interfaces(node)
    return interfaces


def main():
    with open(rf'D:\Projects\wallpyper\src\libs\ctyped\interface.pyi') as file:
        data = file.read()
    tree = ast.parse(data)
    interfaces = _get_interfaces(tree)
    with open('interfaces.json', 'w') as file:
        json.dump(interfaces, file, indent=2)


def _test():
    bench()


if __name__ == '__main__':
    _test()
