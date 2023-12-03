
class Monkey:

    def __init__(self, monkey_id: int, items: list, worry_op: str, div: int, throw_to: list):
        self.monkey_id = monkey_id
        self.start_items = items
        self.worry_op = worry_op
        self.divisor = div
        self.throw_to = throw_to
        self.inspect_count = 0

    def add_item(self, item:int):
        self.start_items.append(item)

    def inspect(self):
        self.inspect_count += 1
