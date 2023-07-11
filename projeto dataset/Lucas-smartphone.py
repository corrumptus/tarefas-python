def get_option() -> int:
    print("1 - Carregar dados do arquivo")
    print("2 - Listar todos os dados")
    print("3 - Listar a média de clockspeed de cada empresa")
    print("4 - Determinar a empresa com mais processadores")
    print("5 - Listar a GPU mais utilizada por cada empresa")
    print("6 - Classificar as CPUs em lenta(<2200), rápida(>=2200, <2800) ou super rápida(>=2800)")
    print("7 - Contar quantas versões existem da CPU Snapdragon")
    print("8 - Determinar qual é a versão mais rápida dentre as CPUs Dimensity")
    print("9 - Listar quais CPUs as empresas usam")
    print("10 - Criar um arquivo com uma lista de todos os dados da apple")
    print("11 - Listar qual é a configuração mais usada por cada empresa")
    print("12 - Determinar qual é o maior clockspeed de cada empresa")
    print("13 - Cadastrar um novo dispositivo")
    print("14 - Determinar qual é o maior clockspeed com o maior número de núcleos de cada empresa")

    choice = input("Digite a opção desejada: ")

    if choice.isnumeric():
        return int(choice)

    return -1

def carrega_data(relative_path: str) -> list[dict[str, str]]:
    array: list[dict[str, str]] = []

    with open(relative_path, "r", encoding="utf-8") as file:
        lines_of_devices = file.readlines()

    name_of_attributes = lines_of_devices[0].split(",")
    lines_of_devices.pop(0)

    for line in lines_of_devices:
        device_line: list[str] = line.split(",")
        array.append({name_of_attributes[i]: device_line[i] for i in range(len(device_line))})

    return array

def persist_data(relative_path: str, array_of_devices: list[dict[str, str]]) -> None:
    header_sequence: list[str] = [
        "rank",
        "company",
        "cpuName",
        "geekbenchSingle",
        "geekbenchMulti",
        "antutu9",
        "coreCount",
        "coreConfig",
        "clockSpeed",
        "classification",
        "gpu"
    ]

    not_classified: bool = True

    lines_of_attr_sequence: list[str] = []

    for device in array_of_devices:
        if "classification" in device:
            not_classified = False

        attr_sequence: list[str] = [device[attr] for attr in header_sequence if attr in device]

        lines_of_attr_sequence.append(",".join(attr_sequence))

    with open(relative_path, "w", encoding="utf-8") as file:
        if not_classified:
            file.write(",".join([attr for attr in header_sequence if attr != "classification"]))
        else:
            file.write(",".join(header_sequence))

        file.write("\n")

        file.write("\n".join(lines_of_attr_sequence))

def persist_new_device(path:str, device: dict[str, str]) -> None:
    header_sequence: list[str] = [
        "rank",
        "company",
        "cpuName",
        "geekbenchSingle",
        "geekbenchMulti",
        "antutu9",
        "coreCount",
        "coreConfig",
        "clockSpeed",
        "classification",
        "gpu"
    ]

    new_line = ",".join([device[attr] for attr in header_sequence if attr in device])

    with open(path, "a", encoding="utf-8") as file:
        file.write(new_line)

def new_device(path: str) -> dict[str, str]:
    with open(path, "r", encoding="utf-8") as file:
        is_classified: bool = "classification" in file.readline().split(",")
        next_rank: int = len(file.readlines())+1

    company = input("Digite o nome da empresa\n")
    name_of_cpu = input("Digite o nome do processador\n")
    geek_bench_single = input("Digite o geekbench single\n")
    geek_bench_multi = input("Digite o geekbench multi\n")
    antutu9 = input("Digite o antutu9\n")
    core_count = input("Digite a quantidade de núcleos\n")
    core_config = input("Digite a configuração dos núcleos Ex.: \"(1+2+3)\"\n")
    clock_speed = input("Digite a velocidade do clock\n")
    gpu = input("Digite o nome do processador gráfico\n")

    device = {
        "rank": str(next_rank),
        "company": company,
        "cpuName": name_of_cpu,
        "geekbenchSingle": geek_bench_single,
        "geekbenchMulti": geek_bench_multi,
        "antutu9": antutu9,
        "coreCount": core_count,
        "coreConfig": core_config,
        "clockSpeed": clock_speed,
        "gpu": gpu
    }

    if is_classified:
        classify_device(device)

    return device

def device_to_string(dict_of_device: dict[str, str]) -> str:
    return str.format(
        """
        --------{}--------
        rank: {}
        company: {}
        cpuName: {}
        geekbenchSingle: {}
        geekbenchMulti: {}
        antutu9: {}
        coreCount: {}
        coreConfig: {}
        clockSpeed: {}
        {}gpu: {}
        {}
        """,
        dict_of_device["cpuName"],
        dict_of_device["rank"],
        dict_of_device["company"],
        dict_of_device["geekbenchSingle"],
        dict_of_device["geekbenchMulti"],
        dict_of_device["antutu9"],
        dict_of_device["coreCount"],
        dict_of_device["coreConfig"],
        dict_of_device["clockSpeed"],
        f'classification: {dict_of_device["classification"]}\n'
            if "classification" in dict_of_device
            else "",
        dict_of_device["gpu"],
        "-"*(len(dict_of_device["cpuName"])+16)
    )

def get_max_of_simple_dict(dictionary: dict[str, int]) -> tuple:
    max_itens: list = ["", -1]

    for key, val in dictionary.items():
        if max_itens[1] < val:
            max_itens = [key, val]

    return tuple(max_itens)

def get_max_of_dict(dictionary: dict[int|float|str, int]) -> tuple:
    max_itens: list = [None, -1]

    for key, val in dictionary.items():
        if max_itens[1] < val:
            max_itens = [key, val]

    return tuple(max_itens)

def get_max_occour_in_list_of_strings(array: list[str]) -> str:
    quantities: dict[str, int] = {}

    for string in array:
        if string not in quantities:
            quantities[string] = 0

        quantities[string] += 1

    return get_max_of_simple_dict(quantities)[0]

def get_sum_and_amount_of_clock_speed_by_company(devices: list[dict[str, str]]) -> dict[str, dict[str, float|int]]:
    companies: dict[str, dict[str, float|int]] = {}
    for device in devices:
        company: str = device["company"]

        if company not in companies:
            companies[company] = {"soma": 0.0, "quantidade": 0}

        companies[company]["soma"] += float(device["clockSpeed"])
        companies[company]["quantidade"] += 1
    return companies

def get_max_occour_in_list(array: list[int|float|str]) -> int|float|str:
    quantities: dict[int|float|str, int] = {}

    for element in array:
        if element not in quantities:
            quantities[element] = 0

        quantities[element] += 1

    return get_max_of_dict(quantities)[0]

def get_list_of_cpus_by_company(devices: list[dict[str, str]]) -> dict[str, list[str]]:
    companies: dict[str, list[str]] = {}

    for device in devices:
        company: str = device["company"]
        name_of_cpu: str = device["cpuName"]

        if company not in companies:
            companies[company] = []

        if name_of_cpu not in companies[company]:
            companies[company].append(name_of_cpu)

    return companies

def get_list_of_gpus_by_company(devices: list[dict[str, str]]) -> dict[str, list[str]]:
    companies: dict[str, list[str]] = {}

    for device in devices:
        company: str = device["company"]
        gpu = device["gpu"]

        if company not in companies:
            companies[company] = []

        if gpu not in companies[company]:
            companies[company].append(gpu)

    return companies

def classify_device(device: dict[str, str]) -> None:
    speed: int = int(device["clockSpeed"])

    if speed < 2200:
        device["classification"] = "lenta"

    elif speed < 2800:
        device["classification"] = "rápida"

    else:
        device["classification"] = "super rápida"

def print_average_clock_speed_by_company(dict_for_average: dict[str, dict[str, float|int]]) -> None:
    for name, sum_and_amount in dict_for_average.items():
        print(str.format(
            "{}: {}",
            name,
            sum_and_amount["soma"]/sum_and_amount["quantidade"]
            if sum_and_amount["quantidade"] > 0
            else 0
        ))

def get_all_snapdragons(devices: list[dict[str, str]]) -> list[str]:
    snapdragons: list[str] = []

    for device in devices:
        name_of_cpu: str = device["cpuName"]

        is_snapdragon: bool = "Snapdragon" in name_of_cpu.title()
        is_in_array: bool = name_of_cpu.title() in snapdragons

        if is_snapdragon and not is_in_array:
            snapdragons.append(name_of_cpu.title())

    return snapdragons

def get_all_dimensitys_and_clock_speed(devices: list[dict[str, str]]) -> dict[str, int]:
    dimensitys: dict[str, int] = {}

    for device in devices:
        name_of_cpu: str = device["cpuName"]
        clock_speed: int = int(device["clockSpeed"])

        is_dimensity: bool = "Dimensity" in name_of_cpu.title()
        is_in_array: bool = name_of_cpu.title() in dimensitys

        if is_dimensity and not is_in_array:
            dimensitys[name_of_cpu] = clock_speed

    return dimensitys

def print_cpus_of_company(company: str, array_of_cpus: list[str]) -> None:
    print(str.format(
        """
        --------{}--------
        {}
        {}
        """,
        company,
        "\n".join(array_of_cpus),
        "-"*(len(company)+16)
    ))

def get_all_devices_from_apple(devices: list[dict[str, str]]) -> list[dict[str, str]]:
    apple_devices: list[dict[str, str]] = []

    for device in devices:
        if device["company"].title() == "Apple":
            apple_devices.append(device)

    return apple_devices

def create_a_file_of_apple_devices(apple_devices: list[dict[str, str]]) -> None:
    with open("apple_devices.txt", "w", encoding="utf-8") as file:
        file.write("cpuName,clockSpeed,gpu\n")

        list_of_lines: list[str] = []

        for device in apple_devices:
            list_of_lines.append(f'{device["cpuName"]},{device["clockSpeed"]},{device["gpu"]}')
            file.write("\n".join(list_of_lines))

def get_all_configurations_by_company(devices: list[dict[str, str]]) -> dict[str, list[str]]:
    configurations: dict[str, list[str]] = {}

    for device in devices:
        company: str = device["company"]
        configuration: str = device["coreConfig"]

        if company not in configurations:
            configurations[company] = []

        configurations[company].append(configuration)

    return configurations

def get_cpus_and_clock_speed_by_company(devices: list[dict[str, str]]) -> dict[str, dict[str, int]]:
    cpus_by_company: dict[str, dict[str, int]] = {}

    for device in devices:
        company: str = device["company"]
        name_of_cpu: str = device["cpuName"]
        clock_speed: int = int(device["clockSpeed"])

        if company not in cpus_by_company:
            cpus_by_company[company] = {}

        if name_of_cpu in cpus_by_company[company]:
            continue

        cpus_by_company[company][name_of_cpu] = clock_speed

    return cpus_by_company

def get_company_clock_and_amount_of_core(devices: list[dict[str, str]]) -> dict[str, dict[str, dict[str, str]]]:
    clock_and_core_configs: dict[str, dict[str, dict[str, str]]] = {}

    for device in devices:
        company: str = device["company"]
        name_of_cpu: str = device["cpuName"]
        clock_speed: str = device["clockSpeed"]
        cores: str = device["coreCount"]

        if company not in clock_and_core_configs:
            clock_and_core_configs[company] = {}

        if name_of_cpu not in clock_and_core_configs[company]:
            clock_and_core_configs[company][name_of_cpu] = {}

        clock_and_core_configs[company][name_of_cpu] = {
            "clockSpeed": clock_speed,
            "coreCount": cores
        }

    return clock_and_core_configs

def get_max_clock_and_amount_of_core(cpus_by_company: dict[str, dict[str, str]]) -> tuple:
    name_of_cpu: str = ""
    clock_speed: int = 0
    core_count: int = 0

    for cpu, attributes in cpus_by_company.items():
        is_fastest: bool = clock_speed < int(attributes["clockSpeed"])
        is_equals_or_gratter: bool = core_count <= int(attributes["coreCount"])

        if is_fastest and is_equals_or_gratter:
            name_of_cpu = cpu
            clock_speed = int(attributes["clockSpeed"])
            core_count = int(attributes["coreCount"])

    return name_of_cpu, clock_speed, core_count

if __name__ == "__main__":
    list_of_devices: list[dict[str, str]] = []
    option: int = 1
    LIST_DEVICES_PATH: str = "Lucas-smartphone.csv"

    while (option := get_option()) != 0:
        if option == 1:
            list_of_devices = carrega_data(LIST_DEVICES_PATH)

        elif option == 2:
            if len(list_of_devices) == 0:
                print("Lista vazia")
                continue

            for object_device in list_of_devices:
                print(device_to_string(object_device))

        elif option == 3:
            dict_for_avg_clock_speed: dict[str, dict[str, float|int]] = {}

            dict_for_avg_clock_speed = get_sum_and_amount_of_clock_speed_by_company(list_of_devices)

            print_average_clock_speed_by_company(dict_for_avg_clock_speed)

        elif option == 4:
            dict_for_max_amount_of_cpu: dict[str, list[str]] = {}

            dict_for_max_amount_of_cpu = get_list_of_cpus_by_company(list_of_devices)

            max_amount = {key: len(val) for key, val in dict_for_max_amount_of_cpu.items()}

            MAX_COMPANY, MAX_AMOUNT_OF_CPU = get_max_of_simple_dict(max_amount)

            print(f"fabricante: {MAX_COMPANY}\nquantidade: {MAX_AMOUNT_OF_CPU}")

        elif option == 5:
            dict_of_all_gpu_by_company: dict[str, list[str]] = {}

            dict_of_all_gpu_by_company = get_list_of_gpus_by_company(list_of_devices)

            for company_name, gpus in dict_of_all_gpu_by_company.items():
                GPU_NAME = get_max_occour_in_list_of_strings(gpus)

                print(f"{company_name}: {GPU_NAME}")

        elif option == 6:
            number_of_non_classified_devices: int = 0

            for object_device in list_of_devices:
                if "classification" in object_device.keys():
                    continue

                number_of_non_classified_devices += 1

                classify_device(object_device)

            if number_of_non_classified_devices > 0:
                persist_data(LIST_DEVICES_PATH, list_of_devices)

        elif option == 7:
            array_of_different_snapdragons: list[str] = []

            array_of_different_snapdragons = get_all_snapdragons(list_of_devices)

            print(len(array_of_different_snapdragons))

        elif option == 8:
            dimensity_clock_speed_dict: dict[str, int] = {}

            dimensity_clock_speed_dict = get_all_dimensitys_and_clock_speed(list_of_devices)

            max_cpu, max_clock_speed = get_max_of_simple_dict(dimensity_clock_speed_dict)

            print(f"CPU: {max_cpu}\nSpeed: {max_clock_speed}")

        elif option == 9:
            dict_for_max_amount_of_cpu: dict[str, list[str]] = {}

            dict_for_max_amount_of_cpu = get_list_of_cpus_by_company(list_of_devices)

            for company_name, cpus in dict_for_max_amount_of_cpu.items():
                print_cpus_of_company(company_name, cpus)

        elif option == 10:
            list_of_apple_devices: list[dict[str, str]] = []

            list_of_apple_devices = get_all_devices_from_apple(list_of_devices)

            create_a_file_of_apple_devices(list_of_apple_devices)

        elif option == 11:
            dict_of_configurations_by_company: dict[str, list[str]] = {}

            dict_of_configurations_by_company = get_all_configurations_by_company(list_of_devices)

            for company_name, configs in dict_of_configurations_by_company.items():
                MOST_OCCOUR = get_max_occour_in_list_of_strings(configs)

                print(f"{company_name}: {MOST_OCCOUR}")

        elif option == 12:
            dict_for_fastest_cpu: dict[str, dict[str, int]] = {}

            dict_for_fastest_cpu = get_cpus_and_clock_speed_by_company(list_of_devices)

            for company_name, cpus in dict_for_fastest_cpu.items():
                max_cpu, max_clock_speed = get_max_of_simple_dict(cpus)

                print(f"{company_name}: {max_cpu} ({max_clock_speed})")

        elif option == 13:
            object_device: dict[str, str] = new_device(LIST_DEVICES_PATH)

            persist_new_device(LIST_DEVICES_PATH, object_device)

            list_of_devices.append(object_device)

        elif option == 14:
            dict_clock_and_amount_of_core: dict[str, dict[str, dict[str, str]]] = {}
            dict_clock_and_amount_of_core = get_company_clock_and_amount_of_core(list_of_devices)

            for company_name, infos in dict_clock_and_amount_of_core.items():
                cpu_name, max_clock, max_amount_of_core = get_max_clock_and_amount_of_core(infos)

                print(f"{company_name}: {max_clock}{max_amount_of_core}({cpu_name})")

        else:
            print("opção inválida")
