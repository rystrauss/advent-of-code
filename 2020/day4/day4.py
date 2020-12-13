import re

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def main():
    with open("input.txt", "r") as fp:
        data = fp.read()

    passports = data.strip().split("\n\n")

    valid_passports_part_1 = 0
    valid_passports_part_2 = 0

    for passport in passports:
        fields = re.split(" |\n", passport)
        split_fields = [field.split(":") for field in fields]
        fields = {pair[0]: pair[1] for pair in split_fields}

        # Part I
        present_passport = all([field in fields.keys() for field in REQUIRED_FIELDS])
        valid_passports_part_1 += int(present_passport)

        if not present_passport:
            continue

        # Part II
        if not 1920 <= int(fields["byr"]) <= 2002:
            continue

        if not 2010 <= int(fields["iyr"]) <= 2020:
            continue

        if not 2020 <= int(fields["eyr"]) <= 2030:
            continue

        height_units = fields["hgt"][-2:]
        if height_units == "cm":
            if not 150 <= int(fields["hgt"][:-2]) <= 193:
                continue
        elif height_units == "in":
            if not 59 <= int(fields["hgt"][:-2]) <= 76:
                continue
        else:
            continue

        if not re.fullmatch("#[\d|a-f]{6}", fields["hcl"]):
            continue

        if fields["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            continue

        if not (len(fields["pid"]) == 9 and fields["pid"].isnumeric()):
            continue

        valid_passports_part_2 += 1

    print("Part I:", valid_passports_part_1)
    print("Part II:", valid_passports_part_2)


if __name__ == "__main__":
    main()
