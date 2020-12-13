def is_valid(next, prev):
    nums = set(prev)

    for i in prev:
        if next - i in nums:
            return True

    return False


def main():
    with open("input.txt", "r") as fp:
        nums = [int(line) for line in fp]

    target = None
    for i in range(25, len(nums)):
        if not is_valid(nums[i], nums[i - 25 : i]):
            target = nums[i]
            break

    print("Part I:", target)

    front, end = 0, 1
    cur_sum = 0

    while end < len(nums):
        while cur_sum < target:
            cur_sum += nums[end - 1]
            end += 1

        while cur_sum > target:
            cur_sum -= nums[front]
            front += 1

        if cur_sum == target:
            break

    min_in_range = min(nums[front:end])
    max_in_range = max(nums[front:end])
    print("Part II:", min_in_range + max_in_range)


if __name__ == "__main__":
    main()
