#FCFS

def fcfs_disk_scheduling(requests, start_position):
    total_head_movement = 0
    current_position = start_position

    for request in requests:
        total_head_movement += abs(current_position - request)
        current_position = request

    return total_head_movement

# Example usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
start_position = 53

total_movement = fcfs_disk_scheduling(requests, start_position)
print(f"Total head movement: {total_movement} cylinders")


#SSTF

import numpy as np

def sstf_disk_scheduling(requests, start_position):
    total_head_movement = 0
    current_position = start_position
    sorted_requests = sorted(requests)

    while sorted_requests:
        # Find the closest request in terms of seek time
        closest_request = min(sorted_requests, key=lambda req: abs(req - current_position))
        total_head_movement += abs(current_position - closest_request)
        current_position = closest_request
        sorted_requests.remove(current_position)

    return total_head_movement

# Example usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
start_position = 53

total_movement = sstf_disk_scheduling(requests, start_position)
print(f"Total head movement: {total_movement} cylinders")

#SCAN 

def scan(requests, head):
  """
  Implements the SCAN disk scheduling algorithm.

  Args:
    requests: A list of track requests.
    head: The initial head position.

  Returns:
    A list of the requests in the order they will be serviced by the disk head.
  """

  # Sort the requests in ascending order.
  requests.sort()

  # Initialize the total seek time.
  total_seek_time = 0

  # Initialize the direction of the disk head.
  direction = "right"

  # While there are still requests to be serviced, do the following:
  while requests:
    # If the disk head is moving to the right, service all requests in the
    # list until we reach the end of the disk or there are no more requests
    # in the list.
    if direction == "right":
      while requests and requests[0] <= head:
        current_request = requests.pop(0)
        total_seek_time += abs(current_request - head)
        head = current_request

    # If the disk head has reached the end of the disk, reverse the direction
    # of the disk head.
    if head == max(requests):
      direction = "left"

    # If the disk head is moving to the left, service all requests in the
    # list until we reach the beginning of the disk or there are no more
    # requests in the list.
    if direction == "left":
      while requests and requests[-1] >= head:
        current_request = requests.pop()
        total_seek_time += abs(current_request - head)
        head = current_request

    # If the disk head has reached the beginning of the disk, reverse the
    # direction of the disk head.
    if head == min(requests):
      direction = "right"

  # Return the total seek time.
  return total_seek_time


# Example usage:

requests = [82, 170, 43, 140, 24, 16, 190]
head = 50

total_seek_time = scan(requests, head)

print(total_seek_time)
