from room import Room
from player import Player
from world import World

import collections 
import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.

# roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}], 12: [(4, 6), {'w': 1, 'e': 13}], 13: [(5, 6), {'w': 12, 'n': 14}], 14: [(5, 7), {'s': 13}], 15: [(2, 6), {'e': 1, 'w': 16}], 16: [(1, 6), {'n': 17, 'e': 15}], 17: [(1, 7), {'s': 16}]}
# roomGraph={494: [(1, 8), {'e': 457}], 492: [(1, 20), {'e': 400}], 493: [(2, 5), {'e': 478}], 457: [(2, 8), {'e': 355, 'w': 494}], 484: [(2, 9), {'n': 482}], 482: [(2, 10), {'s': 484, 'e': 404}], 486: [(2, 13), {'e': 462}], 479: [(2, 15), {'e': 418}], 465: [(2, 16), {'e': 368}], 414: [(2, 19), {'e': 365}], 400: [(2, 20), {'e': 399, 'w': 492}], 451: [(2, 21), {'e': 429}], 452: [(2, 22), {'e': 428}], 478: [(3, 5), {'e': 413, 'w': 493}], 393: [(3, 6), {'e': 375}], 437: [(3, 7), {'e': 347}], 355: [(3, 8), {'e': 312, 'w': 457}], 433: [(3, 9), {'e': 372}], 404: [(3, 10), {'n': 339, 'w': 482}], 339: [(3, 11), {'s': 404, 'e': 314}], 367: [(3, 12), {'n': 462, 'e': 344}], 462: [(3, 13), {'s': 367, 'w': 486}], 463: [(3, 14), {'e': 458, 'n': 418}], 418: [(3, 15), {'e': 349, 'w': 479}], 368: [(3, 16), {'n': 436, 'e': 284, 'w': 465}], 436: [(3, 17), {'s': 368}], 447: [(3, 18), {'n': 365}], 365: [(3, 19), {'s': 447, 'e': 333, 'w': 414}], 399: [(3, 20), {'e': 358, 'w': 400}], 429: [(3, 21), {'n': 428, 'w': 451}], 428: [(3, 22), {'s': 429, 'e': 411, 'w': 452}], 419: [(4, 4), {'n': 413}], 413: [(4, 5), {'n': 375, 's': 419, 'w': 478}], 375: [(4, 6), {'n': 347, 's': 413, 'w': 393}], 347: [(4, 7), {'n': 312, 's': 375, 'w': 437}], 312: [(4, 8), {'s': 347, 'e': 299, 'w': 355}], 372: [(4, 9), {'e': 263, 'w': 433}], 258: [(4, 10), {'e': 236}], 314: [(4, 11), {'e': 220, 'w': 339}], 344: [(4, 12), {'n': 359, 'e': 230, 'w': 367}], 359: [(4, 13), {'n': 458, 's': 344}], 458: [(4, 14), {'s': 359, 'w': 463}], 349: [(4, 15), {'n': 284, 'w': 418}], 284: [(4, 16), {'n': 470, 's': 349, 'e': 254, 'w': 368}], 470: [(4, 17), {'s': 284}], 301: [(4, 18), {'e': 187}], 333: [(4, 19), {'n': 358, 'e': 303, 'w': 365}], 358: [(4, 20), {'n': 397, 's': 333, 'w': 399}], 397: [(4, 21), {'s': 358}], 411: [(4, 22), {'e': 324, 'w': 428}], 396: [(4, 23), {'e': 391}], 449: [(5, 4), {'n': 432, 'e': 450}], 432: [(5, 5), {'n': 405, 's': 449, 'e': 473}], 405: [(5, 6), {'n': 356, 's': 432}], 356: [(5, 7), {'n': 299, 's': 405}], 299: [(5, 8), {'n': 263, 's': 356, 'w': 312}], 263: [(5, 9), {'n': 236, 's': 299, 'w': 372}], 236: [(5, 10), {'s': 263, 'e': 216, 'w': 258}], 220: [(5, 11), {'n': 230, 'e': 215, 'w': 314}], 230: [(5, 12), {'s': 220, 'w': 344}], 266: [(5, 13), {'n': 379, 'e': 260}], 379: [(5, 14), {'s': 266}], 274: [(5, 15), {'e': 222}], 254: [(5, 16), {'e': 205, 'w': 284}], 227: [(5, 17), {'e': 194}], 187: [(5, 18), {'n': 303, 'e': 167, 'w': 301}], 303: [(5, 19), {'n': 352, 's': 187, 'w': 333}], 352: [(5, 20), {'s': 303}], 357: [(5, 21), {'e': 342}], 324: [(5, 22), {'n': 391, 'e': 289, 'w': 411}], 391: [(5, 23), {'n': 489, 's': 324, 'w': 396}], 489: [(5, 24), {'n': 491, 's': 391}], 491: [(5, 25), {'s': 489}], 450: [(6, 4), {'w': 449}], 473: [(6, 5), {'w': 432}], 423: [(6, 6), {'e': 395}], 469: [(6, 7), {'e': 362}], 310: [(6, 8), {'n': 271}], 271: [(6, 9), {'s': 310, 'e': 217}], 216: [(6, 10), {'e': 213, 'w': 236}], 215: [(6, 11), {'n': 243, 'e': 177, 'w': 220}], 243: [(6, 12), {'s': 215}], 260: [(6, 13), {'n': 226, 'w': 266}], 226: [(6, 14), {'s': 260, 'e': 225}], 222: [(6, 15), {'e': 190, 'w': 274}], 205: [(6, 16), {'e': 162, 'w': 254}], 194: [(6, 17), {'e': 128, 'w': 227}], 167: [(6, 18), {'e': 108, 'w': 187}], 171: [(6, 19), {'e': 168}], 297: [(6, 20), {'e': 207}], 342: [(6, 21), {'e': 221, 'w': 357}], 289: [(6, 22), {'n': 319, 'e': 250, 'w': 324}], 319: [(6, 23), {'n': 441, 's': 289}], 441: [(6, 24), {'s': 319}], 453: [(6, 25), {'e': 351}], 395: [(7, 6), {'n': 362, 'w': 423}], 362: [(7, 7), {'n': 327, 's': 395, 'w': 469}], 327: [(7, 8), {'s': 362, 'e': 256}], 217: [(7, 9), {'n': 213, 'w': 271}], 213: [(7, 10), {'s': 217, 'e': 209, 'w': 216}], 177: [(7, 11), {'e': 156, 'w': 215}], 180: [(7, 12), {'e': 164}], 235: [(7, 13), {'e': 158}], 225: [(7, 14), {'e': 105, 'w': 226}], 190: [(7, 15), {'e': 129, 'w': 222}], 162: [(7, 16), {'n': 128, 'w': 205}], 128: [(7, 17), {'s': 162, 'e': 92, 'w': 194}], 108: [(7, 18), {'e': 81, 'w': 167}], 168: [(7, 19), {'n': 207, 'e': 137, 'w': 171}], 207: [(7, 20), {'s': 168, 'w': 297}], 221: [(7, 21), {'n': 250, 'e': 174, 'w': 342}], 250: [(7, 22), {'n': 295, 's': 221, 'w': 289}], 295: [(7, 23), {'n': 332, 's': 250}], 332: [(7, 24), {'n': 351, 's': 295}], 351: [(7, 25), {'n': 417, 's': 332, 'w': 453}], 417: [(7, 26), {'n': 442, 's': 351}], 442: [(7, 27), {'s': 417}], 410: [(8, 5), {'e': 406}], 323: [(8, 6), {'n': 279}], 279: [(8, 7), {'n': 256, 's': 323}], 256: [(8, 8), {'n': 241, 's': 279, 'w': 327}], 241: [(8, 9), {'s': 256, 'e': 193}], 209: [(8, 10), {'n': 156, 'w': 213}], 156: [(8, 11), {'s': 209, 'e': 149, 'w': 177}], 164: [(8, 12), {'n': 158, 'w': 180}], 158: [(8, 13), {'s': 164, 'e': 126, 'w': 235}], 105: [(8, 14), {'n': 129, 'e': 104, 'w': 225}], 129: [(8, 15), {'s': 105, 'w': 190}], 100: [(8, 16), {'n': 92}], 92: [(8, 17), {'n': 81, 's': 100, 'w': 128}], 81: [(8, 18), {'n': 137, 's': 92, 'e': 45, 'w': 108}], 137: [(8, 19), {'s': 81, 'w': 168}], 124: [(8, 20), {'n': 174, 'e': 112}], 174: [(8, 21), {'n': 277, 's': 124, 'w': 221}], 277: [(8, 22), {'n': 331, 's': 174}], 331: [(8, 23), {'n': 387, 's': 277}], 387: [(8, 24), {'n': 444, 's': 331}], 444: [(8, 25), {'s': 387}], 422: [(8, 26), {'n': 461, 'e': 394}], 461: [(8, 27), {'s': 422}], 406: [(9, 5), {'n': 315, 'w': 410}], 315: [(9, 6), {'n': 269, 's': 406, 'e': 335}], 269: [(9, 7), {'n': 203, 's': 315}], 203: [(9, 8), {'n': 193, 's': 269}], 193: [(9, 9), {'n': 191, 's': 203, 'w': 241}], 191: [(9, 10), {'n': 149, 's': 193}], 149: [(9, 11), {'n': 135, 's': 191, 'w': 156}], 135: [(9, 12), {'n': 126, 's': 149}], 126: [(9, 13), {'n': 104, 's': 135, 'w': 158}], 104: [(9, 14), {'n': 89, 's': 126, 'w': 105}], 89: [(9, 15), {'n': 72, 's': 104}], 72: [(9, 16), {'n': 69, 's': 89}], 69: [(9, 17), {'s': 72, 'e': 41}], 45: [(9, 18), {'n': 85, 'e': 40, 'w': 81}], 85: [(9, 19), {'s': 45}], 112: [(9, 20), {'n': 210, 'e': 106, 'w': 124}], 210: [(9, 21), {'s': 112}], 208: [(9, 22), {'n': 307, 'e': 166}], 307: [(9, 23), {'s': 208}], 341: [(9, 24), {'e': 316}], 374: [(9, 25), {'e': 340}], 394: [(9, 26), {'n': 426, 'e': 318, 'w': 422}], 426: [(9, 27), {'s': 394}], 477: [(9, 29), {'e': 443}], 485: [(10, 3), {'e': 481}], 346: [(10, 5), {'n': 335}], 335: [(10, 6), {'s': 346, 'e': 378, 'w': 315}], 369: [(10, 7), {'n': 247}], 247: [(10, 8), {'s': 369, 'e': 234}], 151: [(10, 9), {'n': 188, 'e': 133}], 188: [(10, 10), {'s': 151}], 183: [(10, 11), {'n': 145}], 145: [(10, 12), {'s': 183, 'e': 113}], 122: [(10, 13), {'n': 99}], 99: [(10, 14), {'n': 83, 's': 122}], 83: [(10, 15), {'s': 99, 'e': 80}], 76: [(10, 16), {'n': 41}], 41: [(10, 17), {'s': 76, 'e': 36, 'w': 69}], 40: [(10, 18), {'n': 74, 'e': 19, 'w': 45}], 74: [(10, 19), {'s': 40}], 106: [(10, 20), {'n': 161, 'e': 79, 'w': 112}], 161: [(10, 21), {'n': 166, 's': 106}], 166: [(10, 22), {'s': 161, 'w': 208}], 292: [(10, 23), {'n': 316, 'e': 185}], 316: [(10, 24), {'s': 292, 'w': 341}], 340: [(10, 25), {'n': 318, 'w': 374}], 318: [(10, 26), {'s': 340, 'e': 199, 'w': 394}], 392: [(10, 27), {'n': 408, 'e': 281}], 408: [(10, 28), {'n': 443, 's': 392}], 443: [(10, 29), {'s': 408, 'w': 477}], 481: [(11, 3), {'n': 472, 'w': 485}], 472: [(11, 4), {'n': 466, 's': 481, 'e': 495}], 466: [(11, 5), {'n': 378, 's': 472}], 378: [(11, 6), {'s': 466, 'w': 335}], 280: [(11, 7), {'n': 234}], 234: [(11, 8), {'n': 133, 's': 280, 'e': 259, 'w': 247}], 133: [(11, 9), {'s': 234, 'e': 118, 'w': 151}], 157: [(11, 10), {'e': 110}], 153: [(11, 11), {'e': 97}], 113: [(11, 12), {'e': 94, 'w': 145}], 68: [(11, 13), {'e': 57}], 58: [(11, 14), {'e': 23}], 80: [(11, 15), {'n': 11, 'w': 83}], 11: [(11, 16), {'s': 80, 'e': 3}], 36: [(11, 17), {'e': 21, 'w': 41}], 19: [(11, 18), {'n': 32, 'e': 15, 'w': 40}], 32: [(11, 19), {'s': 19}], 79: [(11, 20), {'e': 46, 'w': 106}], 63: [(11, 21), {'n': 140, 'e': 61}], 140: [(11, 22), {'s': 63}], 185: [(11, 23), {'n': 195, 'e': 155, 'w': 292}], 195: [(11, 24), {'s': 185}], 328: [(11, 25), {'e': 200}], 199: [(11, 26), {'n': 281, 'e': 197, 'w': 318}], 281: [(11, 27), {'n': 350, 's': 199, 'w': 392}], 350: [(11, 28), {'n': 425, 's': 281}], 425: [(11, 29), {'n': 434, 's': 350}], 434: [(11, 30), {'s': 425}], 495: [(12, 4), {'w': 472}], 415: [(12, 5), {'n': 306}], 306: [(12, 6), {'n': 291, 's': 415}], 291: [(12, 7), {'n': 259, 's': 306}], 259: [(12, 8), {'s': 291, 'w': 234}], 118: [(12, 9), {'n': 110, 'e': 218, 'w': 133}], 110: [(12, 10), {'n': 97, 's': 118, 'w': 157}], 97: [(12, 11), {'n': 94, 's': 110, 'w': 153}], 94: [(12, 12), {'n': 57, 's': 97, 'w': 113}], 57: [(12, 13), {'n': 23, 's': 94, 'w': 68}], 23: [(12, 14), {'s': 57, 'e': 6, 'w': 58}], 16: [(12, 15), {'e': 8}], 3: [(12, 16), {'n': 21, 'e': 0, 'w': 11}], 21: [(12, 17), {'s': 3, 'w': 36}], 15: [(12, 18), {'e': 13, 'w': 19}], 47: [(12, 19), {'e': 14}], 46: [(12, 20), {'n': 61, 'e': 17, 'w': 79}], 61: [(12, 21), {'n': 82, 's': 46, 'w': 63}], 82: [(12, 22), {'n': 155, 's': 61}], 155: [(12, 23), {'s': 82, 'w': 185}], 175: [(12, 24), {'n': 200, 'e': 141}], 200: [(12, 25), {'s': 175, 'e': 204, 'w': 328}], 197: [(12, 26), {'e': 165, 'w': 199}], 223: [(12, 27), {'n': 483, 'e': 169}], 483: [(12, 28), {'s': 223}], 488: [(13, 4), {'n': 409}], 409: [(13, 5), {'n': 345, 's': 488}], 345: [(13, 6), {'n': 261, 's': 409}], 261: [(13, 7), {'n': 252, 's': 345}], 252: [(13, 8), {'n': 218, 's': 261}], 218: [(13, 9), {'n': 144, 's': 252, 'w': 118}], 144: [(13, 10), {'n': 134, 's': 218}], 134: [(13, 11), {'n': 65, 's': 144}], 65: [(13, 12), {'n': 62, 's': 134}], 62: [(13, 13), {'n': 6, 's': 65}], 6: [(13, 14), {'s': 62, 'e': 5, 'w': 23}], 8: [(13, 15), {'n': 0, 'w': 16}], 0: [(13, 16), {'n': 4, 's': 8, 'e': 1, 'w': 3}], 4: [(13, 17), {'s': 0}], 13: [(13, 18), {'n': 14, 'e': 9, 'w': 15}], 14: [(13, 19), {'n': 17, 's': 13, 'w': 47}], 17: [(13, 20), {'n': 33, 's': 14, 'e': 28, 'w': 46}], 33: [(13, 21), {'s': 17}], 102: [(13, 22), {'n': 107, 'e': 64}], 107: [(13, 23), {'n': 141, 's': 102}], 141: [(13, 24), {'s': 107, 'w': 175}], 204: [(13, 25), {'w': 200}], 165: [(13, 26), {'n': 169, 'e': 163, 'w': 197}], 169: [(13, 27), {'n': 385, 's': 165, 'w': 223}], 385: [(13, 28), {'s': 169}], 497: [(13, 30), {'e': 366}], 424: [(14, 4), {'n': 322}], 322: [(14, 5), {'s': 424, 'e': 276}], 290: [(14, 6), {'n': 264}], 264: [(14, 7), {'n': 244, 's': 290}], 244: [(14, 8), {'s': 264, 'e': 232}], 181: [(14, 9), {'n': 179}], 179: [(14, 10), {'n': 96, 's': 181, 'e': 201}], 96: [(14, 11), {'n': 66, 's': 179}], 66: [(14, 12), {'n': 50, 's': 96}], 50: [(14, 13), {'n': 5, 's': 66, 'e': 70}], 5: [(14, 14), {'n': 2, 's': 50, 'w': 6}], 2: [(14, 15), {'n': 1, 's': 5, 'e': 10}], 1: [(14, 16), {'n': 7, 's': 2, 'e': 22, 'w': 0}], 7: [(14, 17), {'n': 9, 's': 1, 'e': 12}], 9: [(14, 18), {'s': 7, 'w': 13}], 30: [(14, 19), {'n': 28}], 28: [(14, 20), {'n': 60, 's': 30, 'w': 17}], 60: [(14, 21), {'n': 64, 's': 28}], 64: [(14, 22), {'n': 111, 's': 60, 'w': 102}], 111: [(14, 23), {'n': 121, 's': 64, 'e': 114}], 121: [(14, 24), {'n': 148, 's': 111, 'e': 123}], 148: [(14, 25), {'n': 163, 's': 121, 'e': 178}], 163: [(14, 26), {'n': 257, 's': 148, 'e': 228, 'w': 165}], 257: [(14, 27), {'n': 388, 's': 163}], 388: [(14, 28), {'s': 257, 'n': 386}], 386: [(14, 29), {'e': 354, 's': 388}], 366: [(14, 30), {'e': 361, 'w': 497}], 467: [(15, 3), {'n': 459}], 459: [(15, 4), {'n': 276, 's': 467}], 276: [(15, 5), {'n': 268, 's': 459, 'w': 322}], 268: [(15, 6), {'n': 265, 's': 276}], 265: [(15, 7), {'n': 232, 's': 268, 'e': 273}], 232: [(15, 8), {'n': 206, 's': 265, 'w': 244}], 206: [(15, 9), {'n': 201, 's': 232}], 201: [(15, 10), {'s': 206, 'w': 179}], 159: [(15, 11), {'n': 116}], 116: [(15, 12), {'n': 70, 's': 159}], 70: [(15, 13), {'s': 116, 'e': 87, 'w': 50}], 38: [(15, 14), {'n': 10}], 10: [(15, 15), {'s': 38, 'w': 2}], 22: [(15, 16), {'w': 1}], 12: [(15, 17), {'n': 20, 'e': 18, 'w': 7}], 20: [(15, 18), {'n': 31, 's': 12, 'e': 26}], 31: [(15, 19), {'n': 37, 's': 20}], 37: [(15, 20), {'n': 91, 's': 31, 'e': 42}], 91: [(15, 21), {'n': 101, 's': 37}], 101: [(15, 22), {'s': 91}], 114: [(15, 23), {'e': 120, 'w': 111}], 123: [(15, 24), {'e': 138, 'w': 121}], 178: [(15, 25), {'w': 148}], 228: [(15, 26), {'n': 253, 'w': 163}], 253: [(15, 27), {'n': 285, 's': 228}], 285: [(15, 28), {'s': 253}], 354: [(15, 29), {'n': 361, 'e': 321, 'w': 386}], 361: [(15, 30), {'s': 354, 'w': 366}], 455: [(16, 4), {'n': 382}], 382: [(16, 5), {'n': 296, 's': 455}], 296: [(16, 6), {'n': 273, 's': 382, 'e': 308}], 273: [(16, 7), {'s': 296, 'e': 298, 'w': 265}], 237: [(16, 8), {'n': 229, 'e': 370}], 229: [(16, 9), {'n': 212, 's': 237}], 212: [(16, 10), {'n': 127, 's': 229}], 127: [(16, 11), {'n': 117, 's': 212, 'e': 173}], 117: [(16, 12), {'n': 87, 's': 127, 'e': 170}], 87: [(16, 13), {'s': 117, 'w': 70}], 54: [(16, 14), {'n': 29}], 29: [(16, 15), {'n': 24, 's': 54}], 24: [(16, 16), {'n': 18, 's': 29, 'e': 25}], 18: [(16, 17), {'s': 24, 'e': 34, 'w': 12}], 26: [(16, 18), {'n': 27, 'w': 20}], 27: [(16, 19), {'s': 26, 'e': 55}], 42: [(16, 20), {'n': 51, 'w': 37}], 51: [(16, 21), {'n': 93, 's': 42}], 93: [(16, 22), {'s': 51}], 120: [(16, 23), {'w': 114}], 138: [(16, 24), {'n': 143, 'e': 139, 'w': 123}], 143: [(16, 25), {'s': 138}], 233: [(16, 26), {'n': 240, 'e': 152}], 240: [(16, 27), {'n': 304, 's': 233}], 304: [(16, 28), {'n': 321, 's': 240}], 321: [(16, 29), {'n': 334, 's': 304, 'w': 354}], 334: [(16, 30), {'s': 321, 'e': 384}], 416: [(17, 4), {'n': 317}], 317: [(17, 5), {'n': 308, 's': 416}], 308: [(17, 6), {'s': 317, 'e': 337, 'w': 296}], 298: [(17, 7), {'e': 360, 'w': 273}], 370: [(17, 8), {'w': 237}], 267: [(17, 9), {'n': 202, 'e': 302}], 202: [(17, 10), {'n': 173, 's': 267, 'e': 249}], 173: [(17, 11), {'s': 202, 'w': 127}], 170: [(17, 12), {'n': 182, 'w': 117}], 182: [(17, 13), {'s': 170, 'e': 211}], 77: [(17, 14), {'n': 43, 'e': 130}], 43: [(17, 15), {'n': 25, 's': 77, 'e': 49}], 25: [(17, 16), {'s': 43, 'w': 24}], 34: [(17, 17), {'n': 35, 'e': 39, 'w': 18}], 35: [(17, 18), {'s': 34, 'e': 44}], 55: [(17, 19), {'n': 56, 'w': 27}], 56: [(17, 20), {'n': 73, 's': 55, 'e': 67}], 73: [(17, 21), {'n': 132, 's': 56}], 132: [(17, 22), {'n': 172, 's': 73}], 172: [(17, 23), {'s': 132}], 139: [(17, 24), {'n': 147, 'e': 176, 'w': 138}], 147: [(17, 25), {'n': 152, 's': 139, 'e': 154}], 152: [(17, 26), {'n': 196, 's': 147, 'w': 233}], 196: [(17, 27), {'n': 278, 's': 152, 'e': 224}], 278: [(17, 28), {'n': 338, 's': 196}], 338: [(17, 29), {'s': 278}], 384: [(17, 30), {'e': 435, 'w': 334}], 460: [(18, 4), {'n': 383}], 383: [(18, 5), {'n': 337, 's': 460}], 337: [(18, 6), {'s': 383, 'w': 308}], 360: [(18, 7), {'n': 364, 'w': 298}], 364: [(18, 8), {'s': 360, 'e': 401}], 302: [(18, 9), {'e': 402, 'w': 267}], 249: [(18, 10), {'w': 202}], 272: [(18, 11), {'n': 248}], 248: [(18, 12), {'n': 211, 's': 272}], 211: [(18, 13), {'s': 248, 'w': 182}], 130: [(18, 14), {'w': 77}], 49: [(18, 15), {'e': 119, 'w': 43}], 52: [(18, 16), {'n': 39}], 39: [(18, 17), {'s': 52, 'e': 71, 'w': 34}], 44: [(18, 18), {'n': 48, 'e': 59, 'w': 35}], 48: [(18, 19), {'s': 44, 'e': 53}], 67: [(18, 20), {'n': 84, 'w': 56}], 84: [(18, 21), {'n': 86, 's': 67}], 86: [(18, 22), {'n': 146, 's': 84, 'e': 95}], 146: [(18, 23), {'s': 86}], 176: [(18, 24), {'w': 139}], 154: [(18, 25), {'n': 192, 'e': 184, 'w': 147}], 192: [(18, 26), {'s': 154, 'e': 239}], 224: [(18, 27), {'n': 287, 'w': 196}], 287: [(18, 28), {'n': 313, 's': 224, 'e': 353}], 313: [(18, 29), {'s': 287}], 435: [(18, 30), {'w': 384}], 464: [(19, 6), {'n': 420}], 420: [(19, 7), {'n': 401, 's': 464}], 401: [(19, 8), {'s': 420, 'e': 427, 'w': 364}], 402: [(19, 9), {'e': 403, 'w': 302}], 371: [(19, 10), {'n': 309, 'e': 430}], 309: [(19, 11), {'n': 286, 's': 371, 'e': 377}], 286: [(19, 12), {'n': 242, 's': 309, 'e': 288}], 242: [(19, 13), {'n': 219, 's': 286}], 219: [(19, 14), {'n': 119, 's': 242, 'e': 305}], 119: [(19, 15), {'s': 219, 'e': 131, 'w': 49}], 115: [(19, 16), {'n': 71, 'e': 160}], 71: [(19, 17), {'s': 115, 'e': 150, 'w': 39}], 59: [(19, 18), {'e': 189, 'w': 44}], 53: [(19, 19), {'n': 75, 'w': 48}], 75: [(19, 20), {'n': 78, 's': 53, 'e': 88}], 78: [(19, 21), {'s': 75, 'e': 90}], 95: [(19, 22), {'n': 109, 'w': 86}], 109: [(19, 23), {'n': 136, 's': 95}], 136: [(19, 24), {'s': 109, 'e': 231}], 184: [(19, 25), {'w': 154}], 239: [(19, 26), {'n': 255, 'e': 336, 'w': 192}], 255: [(19, 27), {'s': 239}], 353: [(19, 28), {'n': 380, 'w': 287}], 380: [(19, 29), {'n': 476, 's': 353, 'e': 445}], 476: [(19, 30), {'s': 380}], 496: [(20, 4), {'n': 475}], 475: [(20, 5), {'n': 448, 's': 496}], 448: [(20, 6), {'n': 438, 's': 475, 'e': 490}], 438: [(20, 7), {'n': 427, 's': 448}], 427: [(20, 8), {'s': 438, 'e': 474, 'w': 401}], 403: [(20, 9), {'e': 439, 'w': 402}], 430: [(20, 10), {'e': 440, 'w': 371}], 377: [(20, 11), {'e': 456, 'w': 309}], 288: [(20, 12), {'n': 326, 'e': 498, 'w': 286}], 326: [(20, 13), {'s': 288}], 305: [(20, 14), {'e': 330, 'w': 219}], 131: [(20, 15), {'e': 329, 'w': 119}], 160: [(20, 16), {'e': 214, 'w': 115}], 150: [(20, 17), {'e': 251, 'w': 71}], 189: [(20, 18), {'e': 275, 'w': 59}], 103: [(20, 19), {'n': 88}], 88: [(20, 20), {'s': 103, 'e': 125, 'w': 75}], 90: [(20, 21), {'n': 98, 'e': 142, 'w': 78}], 98: [(20, 22), {'n': 186, 's': 90}], 186: [(20, 23), {'s': 98, 'e': 262}], 231: [(20, 24), {'n': 282, 'e': 294, 'w': 136}], 282: [(20, 25), {'s': 231}], 336: [(20, 26), {'n': 373, 'e': 421, 'w': 239}], 373: [(20, 27), {'s': 336}], 480: [(20, 28), {'n': 445}], 445: [(20, 29), {'s': 480, 'e': 446, 'w': 380}], 490: [(21, 6), {'w': 448}], 474: [(21, 8), {'w': 427}], 439: [(21, 9), {'w': 403}], 440: [(21, 10), {'w': 430}], 456: [(21, 11), {'w': 377}], 498: [(21, 12), {'w': 288}], 348: [(21, 13), {'n': 330}], 330: [(21, 14), {'s': 348, 'e': 454, 'w': 305}], 329: [(21, 15), {'e': 407, 'w': 131}], 214: [(21, 16), {'e': 246, 'w': 160}], 251: [(21, 17), {'w': 150}], 275: [(21, 18), {'e': 283, 'w': 189}], 198: [(21, 19), {'n': 125, 'e': 270}], 125: [(21, 20), {'s': 198, 'e': 238, 'w': 88}], 142: [(21, 21), {'n': 245, 'w': 90}], 245: [(21, 22), {'s': 142, 'e': 343}], 262: [(21, 23), {'e': 390, 'w': 186}], 294: [(21, 24), {'n': 363, 'e': 311, 'w': 231}], 363: [(21, 25), {'s': 294}], 421: [(21, 26), {'w': 336}], 446: [(21, 29), {'w': 445}], 454: [(22, 14), {'w': 330}], 407: [(22, 15), {'w': 329}], 246: [(22, 16), {'n': 325, 'e': 412, 'w': 214}], 325: [(22, 17), {'s': 246}], 283: [(22, 18), {'e': 376, 'w': 275}], 270: [(22, 19), {'e': 300, 'w': 198}], 238: [(22, 20), {'n': 381, 'e': 293, 'w': 125}], 381: [(22, 21), {'s': 238, 'e': 431}], 343: [(22, 22), {'w': 245}], 390: [(22, 23), {'e': 398, 'w': 262}], 311: [(22, 24), {'n': 389, 'e': 499, 'w': 294}], 389: [(22, 25), {'s': 311}], 412: [(23, 16), {'w': 246}], 468: [(23, 17), {'n': 376}], 376: [(23, 18), {'s': 468, 'w': 283}], 300: [(23, 19), {'e': 320, 'w': 270}], 293: [(23, 20), {'w': 238}], 431: [(23, 21), {'w': 381}], 487: [(23, 22), {'n': 398}], 398: [(23, 23), {'s': 487, 'w': 390}], 499: [(23, 24), {'w': 311}], 471: [(24, 18), {'n': 320}], 320: [(24, 19), {'s': 471, 'w': 300}]}

world.loadGraph(roomGraph)
world.printRooms()
player = Player("Name", world.startingRoom)


# USEFUL COMMANDS
# player.currentRoom.id 
# player.currentRoom.getExits()
# player.travel(direction)

# traversalPath = []

previous_room_id = 0
previous_exit_move = 'NONE'
previous_exit_move_full = 'NONE'

# Template for key-value pairs of a new 'room' entry
room_entry_template = {'n': '?',
                       's': '?', 
                       'e': '?', 
                       'w': '?'} 

def check_visited(dictionary, room):
    if room in dictionary:
        print(f"Room # {room} has ALREADY been visited.")
        return f"Visited: {True} \n"
    else:
        print(f"Room # {room} has NOT yet been visited.")
        return f"Visited: {False} \n"

def check_unexplored(dictionary, room):
    if room in dictionary:
        for _, value in dictionary.items():
            if 'n' or 's' or 'e' or 'w' in value:
                for key2, value in value.items():
                    if '?' in value:
                        print(f"Room # {room} has an UNEXPLORED exit facing '{key2}'!")
                        return f"Unexplored Exit Available: {True} \n"

                print(f"All exits at room # {room} have been explored.")
                return f"Unexplored Exit Available: {False} \n"
    else:
        return f"Room # {room} isn't in the dictionary of visited rooms.\n"

# Prints any nested dictionaries in a readable way
def print_nested(val, nesting = -5):
    if type(val) == dict:
	    print("")
	    nesting += 5
	    for k in val:
		    print(nesting * ' ', end='')
		    print(k, end=': ')
		    print_nested(val[k],nesting)
    else:
	    print(val)
 
# Prints current status of player regarding: rooms, moves, & exits    
def get_current_status(graph, traversalPath):
    # print("\n------------------CURRENT STATUS--------------------")
    # print("Previous Exit Move: \t\t\t", previous_exit_move_full)
    # print("Previous Room #: \t\t\t", previous_room_id)
    # print("Current Room #: \t\t\t", player.currentRoom.id)
    # print("\nTotal # of Exits: \t\t\t", len(player.currentRoom.getExits()))
    # print("Available Exits: ", player.currentRoom.getExits())
    # random_exit_array = random.sample(player.currentRoom.getExits(), 1)
    # random_exit_full = get_full_direction(random_exit_array[0])
    # print("Random Future Exit Move: \t\t", random_exit_full)
    # print("\nTotal # of Previous Moves: \t", len(traversalPath))
    # print("List of All Previous Moves: \n\t", traversalPath)
    # print("\nDictionary of Previously Visited Rooms:")
    # print_nested(graph)
    # print("\n------------------------------------------------------")
    # print("----------------------------------------------------------------\n\n")
    pass
        
def get_full_direction(previous_exit_move):
    if previous_exit_move == "n":
        return "NORTH"
    elif previous_exit_move == "s":
        return "SOUTH"
    elif previous_exit_move == "e":
        return "EAST"
    elif previous_exit_move == "w":
        return "WEST"
     
def get_opposite_room_key_value(previous_exit_move):
    if previous_exit_move == "n":
        return "s"
    elif previous_exit_move == "s":
        return "n"
    elif previous_exit_move == "e":
        return "w"
    elif previous_exit_move == "w":
        return "e"

# Use Depth First Traversal (DFT)
# Use a DEQUE instead of a STACK for DFT
print("\n----------------------------------------------------------------")
print("\n************** WELCOME TO TICO'S ADVENTURE GAME! ***************\n")
print("----------------------------------------------------------------")
# Creates a graph to store previously visited rooms
room_graph = {}  
# Creates the FIRST 'room' entry in our adjacency dictionary
room_graph[player.currentRoom.id] = room_entry_template 
# Creates an empty DEQUE to store our previous moves
traversalPath = collections.deque() 
# While there are < 500 'room' entries in the dictionary..
while len(room_graph) < 500:
    # Prints out the player's current status regarding: rooms, moves, and exits
    print("\n------------------CURRENT STATUS--------------------")
    print("Previous Exit Move: \t\t\t", previous_exit_move_full)
    print("Previous Room #: \t\t\t", previous_room_id)
    print("Current Room #: \t\t\t", player.currentRoom.id)
    print("\nTotal # of Exits: \t\t\t", len(player.currentRoom.getExits()))
    print("Available Exits: ", player.currentRoom.getExits())
    random_exit_array = random.sample(player.currentRoom.getExits(), 1)
    random_exit_full = get_full_direction(random_exit_array[0])
    print("Random Future Exit Move: \t\t", random_exit_full)
    print("\nTotal # of Previous Moves: \t", len(traversalPath))
    print("List of All Previous Moves: \n\t", traversalPath)
    print("\nDictionary of Previously Visited Rooms:")
    print_nested(room_graph)
    print("\n------------------------------------------------------")
    print("----------------------------------------------------------------\n\n")
    
    # Sets ID of current room to previous_room_id BEFORE moving
    previous_room_id = player.currentRoom.id   
    # Sets randomly chosen exit direction to future direction_to_travel
    direction_to_travel = random_exit_array[0]  
    # Spells out the full word of the 'future exit move' direction
    direction_to_travel_full = get_full_direction(direction_to_travel)
    
    # Stores the previous move before player makes the move
    previous_exit_move = direction_to_travel  
    # Spells out the full word of the 'previous exit move' direction
    previous_exit_move_full = get_full_direction(previous_exit_move)
    
    player.travel(direction_to_travel)  # Moves the player!
    traversalPath.append(direction_to_travel)  # Adds the player's RECENT move to the 'traversalPath'
    print(f"\n--------------PLAYER MOVEMENT ALERT----------------")
    print(f"\nYou just moved {direction_to_travel_full} from Room # {previous_room_id} to get to Room # {player.currentRoom.id}!\n")
    
    # While the DEQUE is not empty...
    while len(traversalPath) > 0:
        #  (a)  Pop the first room
        # current_room = traversalPath.pop()
        #  (b)  If that room has not been visited...
        if (check_visited(room_graph, player.currentRoom.id) == False):
            #  (i)  Create a room entry for it in the 'visited' dictionary
            room_graph[player.currentRoom.id] = room_entry_template  # Creates a new 'room' entry for the current room
            print("Added Room: ", player.currentRoom.id)
            #  (ii)  Then, add previous moves to the end of the DEQUE
            # for neighbor in graph[current_room]:
            #     s.push(neighbor)
        else: 
            print("All rooms have been visited and all exits have been explored.")

print(check_unexplored(room_graph, 0))
print(check_unexplored(room_graph, 1))
print(check_visited(room_graph, 0))
print(check_visited(room_graph, 1))
      


# graph = {}  # Creates our graph
# graph[player.currentRoom.id] = room_entry_template 
# print("\n------------------CURRENT STATUS--------------------")
# print("Previous Exit Move: \t\t\t", previous_exit_move_full)
# print("Previous Room #: \t\t\t", previous_room_id)
# print("Current Room #: \t\t\t", player.currentRoom.id)
# print("\nTotal # of Exits: \t\t\t", len(player.currentRoom.getExits()))
# print("Available Exits: ", player.currentRoom.getExits())
# random_exit_array = random.sample(player.currentRoom.getExits(), 1)
# random_exit_full = get_full_direction(random_exit_array[0])
# print("Random Future Exit Move: \t\t", random_exit_full)
# print("\nTotal # of Previous Moves: \t", len(traversalPath))
# print("List of All Previous Moves: \n\t", traversalPath)
# print("\nDictionary of Previously Visited Rooms:")
# print_nested(graph)
# print("\n------------------------------------------------------")
# print("----------------------------------------------------------------\n\n")


# previous_room_id = player.currentRoom.id  # Sets ID of current room to previous_room_id BEFORE traveling 
# direction_to_travel = random_exit_array[0]  # Sets randomly chosen exit direction to future direction_to_travel BEFORE traveling
# direction_to_travel_full = get_full_direction(direction_to_travel)

# previous_exit_move = direction_to_travel  # Stores the previous move before player makes the move
# previous_exit_move_full = get_full_direction(previous_exit_move)

# player.travel(direction_to_travel)  # Moves the player!
# traversalPath.append(direction_to_travel)  # Adds the player's RECENT move to the 'traversalPath'
# print(f"\n--------------PLAYER MOVEMENT ALERT----------------")
# print(f"\nYou just moved {direction_to_travel_full} from Room # {previous_room_id} to get to Room # {player.currentRoom.id}!\n")

# graph[player.currentRoom.id] = room_entry_template  # Creates a new 'room' entry for the current room

# print("previous exit move: ", previous_exit_move)
# graph[previous_room_id][get_opposite_room_key_value(previous_exit_move)] = player.currentRoom.id
# print("previous exit move: ", previous_exit_move)
# print("Current Room: ", player.currentRoom.id)
# graph[player.currentRoom.id][direction_to_travel] = previous_room_id
# print("------------------CURRENT STATUS--------------------")
# print("Previous Exit Move: \t\t\t", previous_exit_move_full)
# print("Previous Room #: \t\t\t", previous_room_id)
# print("Current Room #: \t\t\t", player.currentRoom.id)
# print("\nTotal # of Exits: \t\t\t", len(player.currentRoom.getExits()))
# print("Available Exits: ", player.currentRoom.getExits())
# random_exit_array = random.sample(player.currentRoom.getExits(), 1)
# random_exit_full = get_full_direction(random_exit_array[0])
# print("Random Future Exit Move: \t\t", random_exit_full)
# print("\nTotal # of Previous Moves: \t", len(traversalPath))
# print("List of All Previous Moves: \n\t", traversalPath)
# print("\nDictionary of Previously Visited Rooms:")
# print_nested(graph)
# print("\n------------------------------------------------------")
# print("----------------------------------------------------------------\n\n")


# previous_room_id = player.currentRoom.id
# direction_to_travel = random_exit_array[0]
# direction_to_travel_full = get_full_direction(direction_to_travel)

# previous_exit_move = direction_to_travel
# previous_exit_move_full = get_full_direction(previous_exit_move)

# player.travel(direction_to_travel)
# traversalPath.append(direction_to_travel)
# print(f"\n--------------PLAYER MOVEMENT ALERT----------------")
# print(f"\nYou just moved {direction_to_travel_full} from Room # {previous_room_id} to get to Room # {player.currentRoom.id}!\n")

# graph[player.currentRoom.id] = room_entry_template

# graph[player.currentRoom.id][previous_exit_move] = previous_room_id
# print("previous exit move: ", previous_exit_move)
# graph[previous_room_id][get_opposite_room_key_value(previous_exit_move)] = player.currentRoom.id
# print("previous exit move: ", previous_exit_move)
# print("------------------CURRENT STATUS--------------------")
# print("Previous Exit Move: \t\t\t", previous_exit_move_full)
# print("Previous Room #: \t\t\t", previous_room_id)
# print("Current Room #: \t\t\t", player.currentRoom.id)
# print("\nTotal # of Exits: \t\t\t", len(player.currentRoom.getExits()))
# print("Available Exits: ", player.currentRoom.getExits())
# random_exit_array = random.sample(player.currentRoom.getExits(), 1)
# random_exit_full = get_full_direction(random_exit_array[0])
# print("Random Future Exit Move: \t\t", random_exit_full)
# print("\nTotal # of Previous Moves: \t", len(traversalPath))
# print("List of All Previous Moves: \n\t", traversalPath)
# print("\nDictionary of Previously Visited Rooms:")
# print_nested(graph)
# print("\n------------------------------------------------------")
# print("----------------------------------------------------------------\n\n")



# previous_room_id = player.currentRoom.id
# direction_to_travel = random_exit_array[0]
# direction_to_travel_full = get_full_direction(direction_to_travel)

# previous_exit_move = direction_to_travel
# previous_exit_move_full = get_full_direction(previous_exit_move)

# player.travel(direction_to_travel)
# traversalPath.append(direction_to_travel)
# print(f"\n--------------PLAYER MOVEMENT ALERT----------------")
# print(f"\nYou just moved {direction_to_travel_full} from Room # {previous_room_id} to get to Room # {player.currentRoom.id}!\n")

# graph[player.currentRoom.id] = room_entry_template

# print("previous exit move: ", previous_exit_move)
# graph[player.currentRoom.id][previous_exit_move] = previous_room_id
# print("previous exit move: ", previous_exit_move)
# graph[previous_room_id][get_opposite_room_key_value(previous_exit_move)] = player.currentRoom.id
# print("------------------CURRENT STATUS--------------------")
# print("Previous Exit Move: \t\t\t", previous_exit_move_full)
# print("Previous Room #: \t\t\t", previous_room_id)
# print("Current Room #: \t\t\t", player.currentRoom.id)
# print("\nTotal # of Exits: \t\t\t", len(player.currentRoom.getExits()))
# print("Available Exits: ", player.currentRoom.getExits())
# random_exit_array = random.sample(player.currentRoom.getExits(), 1)
# random_exit_full = get_full_direction(random_exit_array[0])
# print("Random Future Exit Move: \t\t", random_exit_full)
# print("\nTotal # of Previous Moves: \t", len(traversalPath))
# print("List of All Previous Moves: \n\t", traversalPath)
# print("\nDictionary of Previously Visited Rooms:")
# print_nested(graph)
# print("\n------------------------------------------------------")
# print("----------------------------------------------------------------\n\n")



print("*************** DID THE TESTS PASS? ****************\n")

# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

    

if len(visited_rooms) == len(roomGraph):
    print("YES!\n \nALL TESTS for 'traversalPath' PASSED: ")
    print("---TOTAL moves: ", len(traversalPath))
    print("---TOTAL rooms visited: ", len(visited_rooms))
    print("Visited Rooms: ", visited_rooms)
else:
    print("NOPE! INCOMPLETE TRAVERSAL!\n \nTESTS for 'traversalPath' FAILED:")
    print(f"---TOTAL # of Unvisited Rooms:\t\t{len(roomGraph) - len(visited_rooms)}")
    print("---Visited Rooms: \n", visited_rooms)
    
print("\n****************************************************\n")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
