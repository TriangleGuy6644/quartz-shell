def main(args):
    if not args:
        print("Usage: calculator [expression]")
        return
    expression = " ".join(args)
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
