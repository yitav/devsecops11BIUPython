import re


class MyBIt:
    def calc_bit(self, bits_amount = 1):
        return bits_amount * 1


class MyByte(MyBIt):
    def calc_bit(self, bits_amount = 1):
        return bits_amount * 8 * super().calc_bit()


class MyKb(MyByte):
    def calc_bit(self, bits_amount=1):
        return bits_amount * 1024 * super().calc_bit()


class MyMb(MyKb):
    def calc_bit(self, bits_amount=1):
        return bits_amount * 1024 * super().calc_bit()


class MyGb(MyMb):
    def calc_bit(self, bits_amount=1):
        return bits_amount * 1024 * super().calc_bit()


RE_INT = re.compile(r'\d+')
RE_WORD = re.compile(r'[A-Za-z]+')

units = ["Bits", "Bytes", "Kb", "Mb", "Gb"]

units_to_class_factory = {
    units[0]: lambda: MyBIt(),
    units[1]: lambda: MyByte(),
    units[2]: lambda: MyKb(),
    units[3]: lambda: MyMb(),
    units[4]: lambda: MyGb(),
}
try:
    f = open("history.txt", "w")

    for i in range(4):
        number_and_unit = input("Please enter your number and unit(Bytes,Kb,Mb,Gb): ")
        number = int(RE_INT.findall(number_and_unit)[0])
        unit = RE_WORD.findall(number_and_unit)[0]
        if unit in units:
            unitObj = units_to_class_factory[unit]()
            conversion_result = unitObj.calc_bit(number)
            # print(conversion_result)
            f.write(number_and_unit + "\n")
            f.write(str(conversion_result) + "\n")
            f.flush()
    f.close()

except IOError:
    print("I/O error")
