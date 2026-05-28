class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        counter = 1
        while counter <= numRows:
            temp_list = [0] * counter
            temp_list[0] = 1
            temp_list[counter - 1] = 1
            for i in range(0, counter - 2):
                if len(result) > 1:
                    temp_list[i + 1] = result[counter - 2][i] + result[counter - 2][i + 1]
            result.append(temp_list)
            counter += 1
        return result

    def getRow(self, rowIndex: int) -> List[int]:
        result = self.generate(rowIndex + 1)
        return result[rowIndex]
