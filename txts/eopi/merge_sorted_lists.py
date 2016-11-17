# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/MergeSortedLists.java
	
	
class Node:
	"""Node class for Linked Lists"""
	
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
		
		
def merge_two_sorted_lists(list1, list2):
	"""Page 113"""
	dummy_head = Node()
	current = dummy_head
	p1 = list1
	p2 = list2
	
	while p1 and p2:
		if p1.data <= p2.data:
			current.next = p1
			p1 = p1.next
		else:
			current.next = p2
			p2 = p2.next
		current = current.next

	# Appends the remaining nodes of p1 or p2
	current.next = p1 if p1 else p2
	return dummy_head.next
	
	
