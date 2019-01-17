def can_sort_by_stack(input_queue):
    stack = []
    output_queue_needed_height = 1
    while len(input_queue) > 0 or len(stack) > 0:
        if len(stack) == 0 or (len(input_queue) > 0 and input_queue[0] < stack[-1]):
            stack.append(input_queue.pop(0))
        elif stack[-1] == output_queue_needed_height:
            stack.pop()
            output_queue_needed_height += 1
        else:
            return False
    return True
