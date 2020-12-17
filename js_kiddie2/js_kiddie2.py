import pprint

b = "155 130 147 244 175 67 0 0 217 92 31 42 174 9 0 78 245 80 191 36 249 87 26 10 243 52 73 52 66 68 68 63 175 0 142 121 58 183 1 114 0 215 0 19 255 0 95 127 51 0 0 223 229 42 68 65 0 0 0 106 78 72 138 66 216 16 78 63 206 127 47 219 0 44 0 112 0 192 194 0 239 55 1 199 116 59 4 212 1 206 156 145 73 77 150 82 160 73 0 243 0 220 133 234 84 0 248 69 0 205 81 108 96 38 70 38 13 0 239 194 144 0 139 0 154 238 121 219 137 127 144 0 0 10 172 7 75 0 217 13 210 65 99 28 0 127 102 71 137 0 230 59 133 0 231 0 139 222 26 229 164 3 222 114 69 73 252 71 193 120 96 237 241 235 30 191 64 249 141 2 226 2 85 205 24 3 68 40 119 0 134 231 41 70 162 95 198 3 253 39 73 67 126 47 6 46 216 253 144 109 141 142 198 35 159 172 235 108 182 111 45 63 13 152 93 136 179 136 114 47 194 224 172 121 126 157 62 250 178 202 157 206 214 115 231 90 172 20 235 207 127 118 231 224 186 151 175 57 129 183 73 55 227 252 199 210 190 54 222 4 10 66 77 151 56 30 158 143 113 236 36 113 178 99 107 22 220 2 108 74 191 36 9 178 213 16 204 125 246 30 122 135 123 55 166 252 151 187 51 210 120 6 70 113 113 91 215 158 63 9 119 37 155 67 198 13 137 247 231 249 201 227 187 13 37 18 34 182 245 112 31 75 223 209 164 235 48 195 91 207 78 252 253 255 159 155 207 205 26 162 194 52 249 111 36 227 62 211 128 234 59 137 56 213 150 231 166 124 104 223 26 244 106 16 140 53 152 207 176 91 157 253 78 233 54 126 241 160 9 161 116 29 202 137 245 126 65 60 9 236 204 157 69 110 30 245 239 226 57 135 151 223 107 82 62 4 239 183 48 78 5 194 204 226 146 79 169 197 126 91 215 223 165 55 201 174 46 68 33 82 51 143 30 228 227 243 73 130 186 15 249 126 76 235 59 215 87 217 156 90 235 231 238 96 231 129 122 4 223 231 220 144 215 41 114 223 237 254 190 124 120 243 101 204 213 52 55 94 14 122 151 17 88 23 145 243 172 129 114 230 206 55 67 90 151 148 149 155 54 161 227 3 126 103 94 115 123 67 55 177 22 143 233 70 164 126 123 143 170 239 181 215 30 98 9 143 107 245 43 113 107 234 59 198 106 144 127 254 223 76 73 93 242 103 82 208 203 99 33 249 181 146 249 251 23 186 108 63 111 210 174 194 54 198 204 242 246 125 228 127 242 60 208 196 135 132 52 78 238 84 59 76 94 233 114 255 194 141 40 213 111 239 144 131 72 232 49 246 246 223 36 99 223 159 63 105 121 125 165 29 251 169 227 36 201 187 59 255 90 254 126 118 106 239 165 74 241 65 153 186 119 250 216 160 42 75 71 3 235 173 64 85 191 154 229 231 16 61 243 238 171 135 44 231 127 149 227 108 179 63 101 242 128 245 15 170 174 249 190 78 167 72 92 165 239 188 42 121 141 253 178 77 110 215 127 83 191 63 73 18 0 0 111 78 77 227 148 60 174 127"
bytes = list(map(int, b.split(" ")))
png_fmt = list(
    map(lambda x: int(x, 16), "89 50 4E 47 0D 0A 1A 0A 0 0 0 D 49 48 44 52".split(" "))
)
LEN = 16
shifter = []

# 候補の数字を探す
candidate_shifter = []
for i in range(LEN):
    num = []
    for j in range(len(bytes)):
        if bytes[j] != png_fmt[i] or j % LEN != i:
            continue
        s = (j - i) // LEN
        if s < 10:
            num.append(s)
    candidate_shifter.append(num)
print("candidate shifter:")
pprint.pprint(candidate_shifter)

# 答えを全通り出す
candidate_keys = []
for i, shifters in enumerate(candidate_shifter):
    keys = []
    for shifter in shifters:
        if i == 0:
            keys.append(str(shifter))
            continue
        for j, v in enumerate(candidate_keys):
            keys.append(v + str(shifter))
    candidate_keys = keys

print("candidate keys:")
print(candidate_keys)

import sys

sys.exit()

# 偶数番目のキーは参照されていないので適当に埋める
# print("keys:")
# for ck in candidate_keys:
#     key = ""
#     for i in range(LEN):
#         key += ck[i]
#         key += "X"
#     pprint.pprint(key)

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://jupiter.challenges.picoctf.org/problem/38421")
for k in candidate_keys:
    elem = driver.find_element_by_id("user_in")
    elem.clear()
    elem.send_keys(k)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    img = driver.find_element_by_id("Area")
    if img.get_attribute("naturalWidth") != "0":
        # qrコードのスクショと読み取り
        png = img.screenshot_as_png
        file_name = f'/tmp/{k}.png'
        with open(file_name, 'wb') as f:
            f.write(png)
        data = decode(Image.open(file_name))
        if not data:
            continue
        code = data[0][0].decode('utf-8', 'ignore')
        print(code)
