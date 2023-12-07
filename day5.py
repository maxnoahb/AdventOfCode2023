import re
import billiard as multiprocessing


def parse_input():
    lines = [i for i in open("inputs/day5_input.txt").read().strip().splitlines() if i]
    # print(lines)
    seeds = lines[0].split(":")[1].strip().split(" ")
    map_regex = "\w+-to-\w+ map:"
    almanac = {}
    for l in lines[1:]:
        if re.findall(map_regex, l):
            split = l.split("-")
            src = split[0]
            dest = split[2].split(" ")[0]
            # print(src, dest)
            almanac[src] = []
        else:
            mapping_list = [int(i) for i in l.split()]
            almanac[src].append(mapping_list)
    # print(almanac)
    final_mapping = {}
    cats = 0
    for src, mapping_list in list(almanac.items()):
        args = [(src, mapping_list, final_mapping)]
        with multiprocessing.Pool(processes=8) as pool:
            pool.map(create_mapping, args)
        print(f"mapped {cats}")
        cats += 1
    # print(final_mapping)
    return seeds, final_mapping


def create_mapping(args):
    src, mapping_list, final_mapping = args
    final_mapping[src] = {}
    for map in mapping_list:
        c = 0
        while c < map[2]:
            final_mapping[src][str(c + map[1])] = c + map[0]
            c += 1


def find_mapping_value(args):
    seed, final_mapping, locations = args
    for src, map in final_mapping.items():
        new_value = map.get(str(seed), seed)
        seed = new_value
        # print(src, new_value)
    locations.append(new_value)


def solve_part1(seeds, final_mapping):
    locations = []
    cats = 0
    for seed in seeds:
        args = [(seed, final_mapping, locations)]
        with multiprocessing.Pool(processes=8) as pool:
            pool.map(find_mapping_value, args)
        print(f"found {cats} values")
        cats += 1
    # print(locations)
    print(min(locations))


if __name__ == "__main__":
    seeds, final_mapping = parse_input()
    solve_part1(seeds, final_mapping)
