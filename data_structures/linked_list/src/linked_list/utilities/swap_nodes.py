from ..linked_list import LinkedList


def swap_nodes(link_list, left, right):
    """
    :param: link_list - pointer to LinkedList
    :param: `left` - indicates position (index) left
    :param: `right` - indicates position (index) right
    return: True if list is changed or None

    Do not create a new linked list
    """

    if left >= right:
        print("Currently the function works only with left and right indices. Please supply proper input.")
        return None

    if left < 0:
        print("Left index must be a positive number or 0")
        return None

    if right < 0:
        print("Right index must be a positive number, greater or equal to 1")
        return None

    if link_list.head is None:
        print("Please provide a LinkedList that is not empty.")
        return None

    # Used both as a counter and LinkedList size
    counter = 0
    elem = link_list.head
    # Initially the prev element should be None
    # (this may cause issue with the Head pointer check!)
    prev_element = None

    # Elements needed for the swap
    first = None
    first_prev = None
    first_next = None
    second = None
    second_prev = None

    while elem is not None:
        if counter == left:
            first_prev = prev_element
            first = elem
            first_next = first.next

        if counter == right:
            second_prev = prev_element
            second = elem
            break

        # Increment Counter and LinkedList
        counter += 1
        prev_element = elem
        elem = elem.next

    if first is None or second is None:
        print("Index numbers are greater than List size!")
        return None

    first.next = second.next

    if first_next is not second:
        second_prev.next = first

    if first_prev is None:
        link_list.head = second
    else:
        first_prev.next = second

    if first_next is second:
        second.next = first
    else:
        second.next = first_next

    return True
