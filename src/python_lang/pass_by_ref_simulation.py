from types import SimpleNamespace  # noqa F401


def foo(n: int) -> None:
    print(f"[foo] x: value={x} type={type(n)} id={id(n)}")
    n = 42
    print(f"[foo] x: value={x} type={type(n)} id={id(n)}")


# def foo(n: int) -> None:
#     global x
#     print(f"[foo] x: value={x} type={type(n)} id={id(n)}")
#     x = 42
#     print(f"[foo] x: value={x} type={type(n)} id={id(n)}")


# def foo(n: int) -> int:
#     print(f"[foo] x: value={n} type={type(n)} id={id(n)}")
#     n = 42
#     print(f"[foo] x: value={n} type={type(n)} id={id(n)}")
#     return n


# def foo(ns: SimpleNamespace) -> None:
#     print(f"[ns] x: value={ns.x} type={type(ns.x)} id={id(ns.x)}")
#     ns.x = 42
#     print(f"[ns] x: value={ns.x} type={type(ns.x)} id={id(ns.x)}")


# def foo(d: dict[str, int]) -> None:
#     print(f"[d] x: value={d['x']} type={type(d['x'])} id={id(d['x'])}")
#     d["x"] = 42
#     print(f"[d] x: value={d['x']} type={type(d['x'])} id={id(d['x'])}")


if __name__ == "__main__":
    x = 5
    print(f"[global] x: value={x} type={type(x)} id={id(x)}")
    foo(x)
    print(f"[global] x: value={x} type={type(x)} id={id(x)}")

    # x = 5
    # print(f"[global] x: value={x} type={type(x)} id={id(x)}")
    # x = foo(x)
    # print(f"[global] x: value={x} type={type(x)} id={id(x)}")

    # ns = SimpleNamespace(x=5)
    # print(f"[ns] x: value={ns.x} type={type(ns.x)} id={id(ns.x)}")
    # foo(ns)
    # print(f"[ns] x: value={ns.x} type={type(ns.x)} id={id(ns.x)}")

    # d = {"x": 5}
    # print(f"[d] x: value={d['x']} type={type(d['x'])} id={id(d['x'])}")
    # foo(d)
    # print(f"[d] x: value={d['x']} type={type(d['x'])} id={id(d['x'])}")
