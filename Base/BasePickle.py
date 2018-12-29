__author__ = "shikun"
import pickle
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def writeSum(init, data=None, path="data.pickle"):
    if init == 0:
        result = data
    else:
        _read = readInfo(path)
        result = _read - 1

    with open(path, 'wb') as f:
        print("------writeSum-------")
        print(result)
        pickle.dump(result, f)


def readSum(path):
    data = {}
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = {}
            print("读取文件错误")
    print("------read-------")
    print(path)
    print(data)
    return data


def readInfo(path):
    data = []
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
            # print(data)
        except EOFError:
            data = []
            # print("读取文件错误")
    print("------read-------")
    print(path)
    print(data)
    return data


def writeInfo(data, path="data.pickle"):
    _read = readInfo(path)
    result = []
    if _read:
        _read.append(data)
        result = _read
    else:
        result.append(data)
    with open(path, 'wb') as f:
        print("------writeInfo-------")
        print(result)
        pickle.dump(result, f)

def writeFlowInfo(upflow, downflow, path="data.pickle"):
    print("---data-----")
    print("上行流量="+str(upflow))
    print("下行流量="+str(downflow))

    _read = readInfo(path)
    result = [[], []]
    if _read:
        _read[0].append(upflow)
        _read[1].append(downflow)
        result = _read
    else:
        result[0].append(upflow)
        result[1].append(downflow)
    with open(path, 'wb') as f:
        print("------writeFlowInfo-------")
        print(result)
        pickle.dump(result, f)


if __name__ == "__main__":
    # readInfo(PATH("../info/DU2TAN15AJ049163_battery.pickle"))
    # readInfo(PATH("../info/emulator-5554_fps.pickle"))
    # readInfo(PATH("../info/emulator-5554_battery.pickle"))
    # readInfo(PATH("../info/emulator-5554_men.pickle"))
    # readInfo(PATH("../info/DU2TAN15AJ049163_men.pickle"))
    # 获取对应的设备下的cpu信息，cpu的信息按照时间节点，先后排序为一个列表
    readInfo(PATH("E:\\Python\\monkeyTest\\info\\37KNW18529001041_cpu.pickle"))
    # readInfo("E:\\Python\\monkeyTest\\info\\info.pickle")
    # readInfo(PATH("../info/DU2TAN15AJ049163_cpu.pickle"))
