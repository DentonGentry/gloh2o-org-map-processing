import glob
import os.path

import pandas as pd
import extract_country_data as ecd

import admin_names

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 40)

gaez_tropical_humid = [
    ["Region", "total", "tropical-humid|AEZ1", "tropical-humid|AEZ2", "tropical-humid|AEZ3", "tropical-humid|AEZ4", "tropical-humid|AEZ5", "tropical-humid|AEZ6", "tropical-humid|AEZ7", "tropical-humid|AEZ8", "tropical-humid|AEZ9", "tropical-humid|AEZ10", "tropical-humid|AEZ11", "tropical-humid|AEZ12", "tropical-humid|AEZ13", "tropical-humid|AEZ14", "tropical-humid|AEZ15", "tropical-humid|AEZ16", "tropical-humid|AEZ17", "tropical-humid|AEZ18", "tropical-humid|AEZ19", "tropical-humid|AEZ20", "tropical-humid|AEZ21", "tropical-humid|AEZ22", "tropical-humid|AEZ23", "tropical-humid|AEZ24", "tropical-humid|AEZ25", "tropical-humid|AEZ26", "tropical-humid|AEZ27", "tropical-humid|AEZ28", "tropical-humid|AEZ29"],
    ["OECD90", 520108, 52651, 52287, 24266, 7019, 19183, 8903, 2575, 80227, 79671, 36976, 10696, 29231, 13566, 3924, 304, 302, 140, 40, 111, 51, 15, 6544, 6498, 3016, 872, 2384, 1106, 320, 77229],
    ["Eastern Europe", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["Asia (Sans Japan)", 5194253, 287156, 234919, 231551, 113294, 145300, 143217, 70074, 327076, 267578, 263741, 129044, 165500, 163126, 79815, 90544, 74073, 73011, 35723, 45815, 45158, 22095, 266815, 218279, 215149, 105269, 135008, 133072, 65110, 1047742],
    ["Middle East and Africa", 9489634, 364595, 443799, 256422, 43439, 162376, 93819, 15893, 814286, 991180, 572693, 97016, 362650, 209535, 35496, 5836, 7103, 4104, 695, 2599, 1502, 254, 303356, 369256, 213352, 36143, 135102, 78061, 13224, 3855849],
    ["Latin America", 11062563, 1627748, 2055087, 782144, 238417, 385083, 146558, 44675, 1324051, 1671659, 636216, 193934, 313236, 119214, 36339, 23790, 30036, 11431, 3485, 5628, 2142, 653, 238256, 300806, 114483, 34897, 56365, 21452, 6539, 638239],
    ["China", 29481, 900, 758, 1151, 634, 552, 839, 462, 1731, 1457, 2213, 1219, 1062, 1613, 889, 387, 326, 495, 273, 238, 361, 199, 621, 522, 793, 437, 381, 578, 319, 8071],
    ["India", 952830, 56311, 67115, 21328, 6159, 52734, 16758, 4839, 25449, 30333, 9639, 2783, 23833, 7574, 2187, 50800, 60547, 19241, 5556, 47572, 15118, 4365, 98695, 117632, 37381, 10794, 92425, 29371, 8481, 27811],
    ["EU", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["USA", 9289, 1476, 998, 752, 218, 173, 130, 38, 1579, 1067, 804, 234, 185, 139, 40, 19, 13, 10, 3, 2, 2, 0, 102, 69, 52, 15, 12, 9, 3, 1145]]
 
gaez_temperate_boreal_humid = [
    ["Region", "total", "temperate/boreal-humid|AEZ1", "temperate/boreal-humid|AEZ2", "temperate/boreal-humid|AEZ3", "temperate/boreal-humid|AEZ4", "temperate/boreal-humid|AEZ5", "temperate/boreal-humid|AEZ6", "temperate/boreal-humid|AEZ7", "temperate/boreal-humid|AEZ8", "temperate/boreal-humid|AEZ9", "temperate/boreal-humid|AEZ10", "temperate/boreal-humid|AEZ11", "temperate/boreal-humid|AEZ12", "temperate/boreal-humid|AEZ13", "temperate/boreal-humid|AEZ14", "temperate/boreal-humid|AEZ15", "temperate/boreal-humid|AEZ16", "temperate/boreal-humid|AEZ17", "temperate/boreal-humid|AEZ18", "temperate/boreal-humid|AEZ19", "temperate/boreal-humid|AEZ20", "temperate/boreal-humid|AEZ21", "temperate/boreal-humid|AEZ22", "temperate/boreal-humid|AEZ23", "temperate/boreal-humid|AEZ24", "temperate/boreal-humid|AEZ25", "temperate/boreal-humid|AEZ26", "temperate/boreal-humid|AEZ27", "temperate/boreal-humid|AEZ28", "temperate/boreal-humid|AEZ29"],
    ["OECD90", 15886657, 1402160, 1392458, 646241, 186936, 510879, 237099, 68585, 2136536, 2121752, 984707, 284843, 778450, 361279, 104506, 109478, 108721, 50457, 14596, 39888, 18512, 5355, 715069, 710121, 329568, 95333, 260536, 120915, 34977, 2056699],
    ["Eastern Europe", 11847020, 1449107, 1457234, 928676, 219279, 240998, 153585, 36265, 1228607, 1235497, 787366, 185913, 204327, 130215, 30746, 27291, 27444, 17490, 4130, 4539, 2892, 683, 486722, 489452, 311921, 73651, 80946, 51586, 12180, 1968277],
    ["Asia (Sans Japan)", 4075076, 226121, 184988, 182335, 89214, 114417, 112776, 55180, 257557, 210704, 207683, 101616, 130323, 128454, 62851, 100762, 82433, 81251, 39755, 50985, 50254, 24589, 177092, 144877, 142799, 69870, 89608, 88323, 43215, 825046],
    ["Middle East and Africa", 2442866, 96236, 117142, 67683, 11466, 42860, 24764, 4195, 214933, 261625, 151164, 25608, 95722, 55307, 9369, 4037, 4914, 2839, 481, 1798, 1039, 176, 61212, 74510, 43051, 7293, 27261, 15751, 2668, 1017762],
    ["Latin America", 3423361, 476782, 601954, 229097, 69834, 112794, 42928, 13086, 387827, 489644, 186353, 56805, 91750, 34919, 10644, 9141, 11541, 4392, 1339, 2163, 823, 251, 124045, 156611, 59604, 18169, 29346, 11169, 3404, 186946],
    ["China", 2431268, 69026, 58083, 88215, 48601, 42352, 64323, 35438, 132734, 111690, 169632, 93456, 81441, 123690, 68145, 40874, 34394, 52237, 28779, 25079, 38089, 20985, 65490, 55107, 83695, 46111, 40182, 61028, 33622, 618768],
    ["India", 773208, 52100, 62096, 19733, 5698, 48790, 15505, 4477, 23546, 28064, 8918, 2575, 22050, 7007, 2023, 37795, 45046, 14315, 4134, 35394, 11247, 3248, 73429, 87518, 27812, 8031, 68764, 21852, 6310, 25731],
    ["EU", 3041133, 405250, 243153, 234528, 55534, 96016, 92610, 21929, 321659, 192998, 186152, 44079, 76211, 73508, 17406, 36800, 22080, 21297, 5043, 8719, 8410, 1991, 304438, 182666, 176186, 41719, 72131, 69572, 16474, 12571],
    ["USA", 5542770, 674440, 455913, 343541, 99799, 78908, 59459, 17273, 721153, 487490, 367336, 106712, 84373, 63577, 18469, 87572, 59198, 44607, 12958, 10246, 7720, 2243, 474523, 320771, 241709, 70217, 55518, 41834, 12153, 523058]]


gaez_tropical_semiarid = [
    ["Region", "total", "tropical-semiarid|AEZ1", "tropical-semiarid|AEZ2", "tropical-semiarid|AEZ3", "tropical-semiarid|AEZ4", "tropical-semiarid|AEZ5", "tropical-semiarid|AEZ6", "tropical-semiarid|AEZ7", "tropical-semiarid|AEZ8", "tropical-semiarid|AEZ9", "tropical-semiarid|AEZ10", "tropical-semiarid|AEZ11", "tropical-semiarid|AEZ12", "tropical-semiarid|AEZ13", "tropical-semiarid|AEZ14", "tropical-semiarid|AEZ15", "tropical-semiarid|AEZ16", "tropical-semiarid|AEZ17", "tropical-semiarid|AEZ18", "tropical-semiarid|AEZ19", "tropical-semiarid|AEZ20", "tropical-semiarid|AEZ21", "tropical-semiarid|AEZ22", "tropical-semiarid|AEZ23", "tropical-semiarid|AEZ24", "tropical-semiarid|AEZ25", "tropical-semiarid|AEZ26", "tropical-semiarid|AEZ27", "tropical-semiarid|AEZ28", "tropical-semiarid|AEZ29"],
    ["OECD90", 4336538, 389795, 387098, 179652, 51967, 142022, 65913, 19066, 593948, 589838, 273744, 79185, 216406, 100434, 29052, 18467, 18340, 8511, 2462, 6729, 3123, 903, 185550, 184266, 85518, 24738, 67605, 31376, 9076, 571754],
    ["Eastern Europe", 2603365, 287123, 288733, 184006, 43447, 47751, 30431, 7185, 243433, 244798, 156007, 36836, 40485, 25800, 6092, 24141, 24277, 15471, 3653, 4015, 2559, 604, 160423, 161323, 102809, 24275, 26680, 17003, 4015, 389990],
    ["Asia (Sans Japan)", 2625710, 146612, 119942, 118222, 57844, 74185, 73121, 35777, 166994, 136616, 134657, 65885, 84498, 83287, 40751, 66387, 54310, 53531, 26192, 33591, 33110, 16200, 109907, 89914, 88625, 43363, 55613, 54815, 26820, 534940],
    ["Middle East and Africa", 6279960, 245360, 298662, 172563, 29233, 109273, 63137, 10696, 547988, 667031, 385403, 65289, 244051, 141010, 23888, 18507, 22527, 13016, 2205, 8242, 4762, 807, 161505, 196590, 113587, 19242, 71928, 41559, 7040, 2594858],
    ["Latin America", 1427174, 209079, 263970, 100464, 30624, 49463, 18825, 5738, 170070, 214720, 81720, 24910, 40234, 15313, 4668, 4949, 6248, 2378, 725, 1171, 446, 136, 30628, 38669, 14717, 4486, 7246, 2758, 841, 81980],
    ["China", 1424976, 45631, 38396, 58315, 32128, 27997, 42522, 23427, 87746, 73834, 112138, 61781, 53837, 81767, 45048, 15115, 12718, 19316, 10642, 9274, 14085, 7760, 24217, 20378, 30949, 17051, 14859, 22567, 12433, 409044],
    ["India", 627107, 28698, 34204, 10869, 3139, 26875, 8540, 2466, 12970, 15458, 4912, 1418, 12146, 3860, 1115, 37911, 45185, 14359, 4146, 35503, 11282, 3258, 73655, 87788, 27897, 8055, 68976, 21919, 6329, 14173],
    ["EU", 51095, 5709, 3426, 3304, 782, 1353, 1305, 309, 4532, 2719, 2623, 621, 1074, 1036, 245, 1500, 900, 868, 206, 355, 343, 81, 6217, 3730, 3598, 852, 1473, 1421, 336, 177],
    ["USA", 1493869, 207127, 140015, 105505, 30649, 24233, 18260, 5305, 221473, 149713, 112812, 32772, 25912, 19525, 5672, 14234, 9622, 7250, 2106, 1665, 1255, 365, 77127, 52137, 39287, 11413, 9024, 6800, 1975, 160636]]


gaez_temperate_boreal_semiarid = [
    ["Region", "total", "temperate/boreal-semiarid|AEZ1", "temperate/boreal-semiarid|AEZ2", "temperate/boreal-semiarid|AEZ3", "temperate/boreal-semiarid|AEZ4", "temperate/boreal-semiarid|AEZ5", "temperate/boreal-semiarid|AEZ6", "temperate/boreal-semiarid|AEZ7", "temperate/boreal-semiarid|AEZ8", "temperate/boreal-semiarid|AEZ9", "temperate/boreal-semiarid|AEZ10", "temperate/boreal-semiarid|AEZ11", "temperate/boreal-semiarid|AEZ12", "temperate/boreal-semiarid|AEZ13", "temperate/boreal-semiarid|AEZ14", "temperate/boreal-semiarid|AEZ15", "temperate/boreal-semiarid|AEZ16", "temperate/boreal-semiarid|AEZ17", "temperate/boreal-semiarid|AEZ18", "temperate/boreal-semiarid|AEZ19", "temperate/boreal-semiarid|AEZ20", "temperate/boreal-semiarid|AEZ21", "temperate/boreal-semiarid|AEZ22", "temperate/boreal-semiarid|AEZ23", "temperate/boreal-semiarid|AEZ24", "temperate/boreal-semiarid|AEZ25", "temperate/boreal-semiarid|AEZ26", "temperate/boreal-semiarid|AEZ27", "temperate/boreal-semiarid|AEZ28", "temperate/boreal-semiarid|AEZ29"],
    ["OECD90", 3665022, 320078, 317864, 147521, 42673, 116621, 54124, 15656, 487718, 484344, 224784, 65023, 177701, 82471, 23856, 35789, 35541, 16495, 4771, 13040, 6052, 1751, 164579, 163440, 75853, 21942, 59964, 27830, 8050, 469493],
    ["Eastern Europe", 4774536, 628068, 631590, 402504, 95039, 104453, 66566, 15718, 532499, 535485, 341258, 80578, 88559, 56437, 13326, 15922, 16011, 10204, 2409, 2648, 1687, 398, 90495, 91002, 57995, 13694, 15050, 9591, 2265, 853085],
    ["Asia (Sans Japan)", 4935041, 333975, 273221, 269303, 131766, 168990, 166567, 81499, 380403, 311204, 306742, 150084, 192483, 189723, 92828, 56249, 46017, 45357, 22192, 28462, 28054, 13726, 100200, 81973, 80797, 39533, 50701, 49974, 24451, 1218568],
    ["Middle East and Africa", 2074003, 73519, 89490, 51707, 8759, 32742, 18918, 3205, 164198, 199868, 115481, 19563, 73127, 42252, 7158, 24625, 29974, 17319, 2934, 10967, 6337, 1073, 80104, 97505, 56338, 9544, 35675, 20613, 3492, 777517],
    ["Latin America", 2563962, 361347, 456212, 173630, 52927, 85485, 32535, 9917, 293928, 371094, 141235, 43052, 69536, 26465, 8067, 21001, 26515, 10091, 3076, 4968, 1891, 576, 70518, 89031, 33884, 10329, 16683, 6349, 1935, 141684],
    ["China", 3668130, 122501, 103080, 156555, 86252, 75162, 114155, 62892, 235564, 198217, 301047, 165858, 144533, 219514, 120938, 30295, 25492, 38717, 21330, 18588, 28231, 15553, 48540, 40844, 62033, 34176, 29782, 45232, 24920, 1098130],
    ["India", 81393, 10962, 13065, 4152, 1199, 10265, 3262, 942, 4954, 5905, 1876, 542, 4639, 1474, 426, 1046, 1247, 396, 114, 980, 311, 90, 2033, 2423, 770, 222, 1904, 605, 175, 5414],
    ["EU", 802983, 106772, 64064, 61791, 14632, 25297, 24400, 5778, 84748, 50849, 49046, 11614, 20079, 19367, 4586, 23325, 13995, 13499, 3196, 5526, 5330, 1262, 67193, 40316, 38886, 9208, 15920, 15355, 3636, 3312],
    ["USA", 1319559, 201040, 135900, 102404, 29749, 23521, 17724, 5149, 214964, 145313, 109497, 31809, 25150, 18951, 5505, 5892, 3983, 3001, 872, 689, 519, 151, 31925, 21581, 16262, 4724, 3735, 2815, 818, 155915]]


gaez_global_arid = [
    ["Region", "total", "arid|AEZ1", "arid|AEZ2", "arid|AEZ3", "arid|AEZ4", "arid|AEZ5", "arid|AEZ6", "arid|AEZ7", "arid|AEZ8", "arid|AEZ9", "arid|AEZ10", "arid|AEZ11", "arid|AEZ12", "arid|AEZ13", "arid|AEZ14", "arid|AEZ15", "arid|AEZ16", "arid|AEZ17", "arid|AEZ18", "arid|AEZ19", "arid|AEZ20", "arid|AEZ21", "arid|AEZ22", "arid|AEZ23", "arid|AEZ24", "arid|AEZ25", "arid|AEZ26", "arid|AEZ27", "arid|AEZ28", "arid|AEZ29"],
    ["OECD90", 2971992, 313752, 311581, 144605, 41829, 114316, 53054, 15347, 478079, 474771, 220341, 63737, 174189, 80841, 23385, 36, 36, 16, 5, 13, 6, 2, 580, 576, 267, 77, 211, 98, 28, 460214],
    ["Eastern Europe", 1575339, 219606, 220838, 140737, 33231, 36522, 23275, 5496, 186190, 187234, 119322, 28174, 30965, 19734, 4659, 5614, 5645, 3598, 849, 934, 595, 140, 1194, 1201, 765, 181, 199, 127, 30, 298284],
    ["Asia (Sans Japan)", 2948213, 200454, 163989, 161638, 79087, 101429, 99975, 48916, 228321, 186787, 184109, 90081, 115530, 113873, 55716, 43884, 35901, 35386, 17314, 22205, 21887, 10709, 46776, 38267, 37718, 18455, 23668, 23329, 11415, 731394],
    ["Middle East and Africa", 13668694, 589685, 717787, 414730, 70257, 262622, 151740, 25705, 1317003, 1603106, 926257, 156911, 586540, 338896, 57410, 18680, 22738, 13138, 2226, 8319, 4807, 814, 37768, 45972, 26562, 4500, 16820, 9719, 1646, 6236337],
    ["Latin America", 1171661, 186156, 235028, 89449, 27266, 44040, 16761, 5109, 151424, 191178, 72760, 22179, 35823, 13634, 4156, 304, 384, 146, 45, 72, 27, 8, 839, 1059, 403, 123, 198, 76, 23, 72992],
    ["China", 1429222, 52136, 43870, 66629, 36708, 31989, 48584, 26767, 100255, 84360, 128124, 70588, 61513, 93424, 51471, 4275, 3598, 5464, 3010, 2623, 3984, 2195, 6850, 5764, 8754, 4823, 4203, 6383, 3517, 467360],
    ["India", 276822, 17087, 20365, 6472, 1869, 16001, 5085, 1468, 7722, 9204, 2925, 845, 7232, 2298, 664, 14369, 17126, 5442, 1572, 13456, 4276, 1235, 27917, 33274, 10574, 3053, 26144, 8308, 2399, 8439],
    ["EU", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["USA", 296294, 48678, 32905, 24795, 7203, 5695, 4291, 1247, 52049, 35185, 26512, 7702, 6090, 4589, 1333, 16, 11, 8, 2, 2, 1, 0, 88, 60, 45, 13, 10, 8, 2, 37752]]


gaez_global_arctic = [
    ["Region", "total", "arctic|AEZ1", "arctic|AEZ2", "arctic|AEZ3", "arctic|AEZ4", "arctic|AEZ5", "arctic|AEZ6", "arctic|AEZ7", "arctic|AEZ8", "arctic|AEZ9", "arctic|AEZ10", "arctic|AEZ11", "arctic|AEZ12", "arctic|AEZ13", "arctic|AEZ14", "arctic|AEZ15", "arctic|AEZ16", "arctic|AEZ17", "arctic|AEZ18", "arctic|AEZ19", "arctic|AEZ20", "arctic|AEZ21", "arctic|AEZ22", "arctic|AEZ23", "arctic|AEZ24", "arctic|AEZ25", "arctic|AEZ26", "arctic|AEZ27", "arctic|AEZ28", "arctic|AEZ29"],
    ["OECD90", 2060794, 217700, 216194, 100336, 29024, 79319, 36812, 10649, 331720, 329425, 152886, 44225, 120863, 56092, 16226, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 319324],
    ["Eastern Europe", 1079999, 152575, 153430, 97779, 23088, 25374, 16171, 3818, 129358, 130084, 82901, 19575, 21513, 13710, 3237, 2, 2, 1, 0, 0, 0, 0, 46, 46, 29, 7, 8, 5, 1, 207237],
    ["Asia (Sans Japan)", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["Middle East and Africa", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["Latin America", 22097, 3504, 4424, 1684, 513, 829, 315, 96, 2850, 3598, 1370, 417, 674, 257, 78, 22, 28, 11, 3, 5, 2, 1, 13, 16, 6, 2, 3, 1, 0, 1374],
    ["China", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["India", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["EU", 27832, 5439, 3264, 3148, 745, 1289, 1243, 294, 4317, 2590, 2499, 592, 1023, 987, 234, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 169],
    ["USA", 188997, 31078, 21008, 15830, 4599, 3636, 2740, 796, 33231, 22464, 16927, 4917, 3888, 2930, 851, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24103]]


spatial = pd.read_csv('results/AEZ-by-country.csv').set_index('Country')
spatial_region = pd.DataFrame(0, index=['OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
    'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
    columns=spatial.columns.copy())
for country, row in spatial.iterrows():
    region = admin_names.region_mapping[country]
    if region is not None:
        spatial_region.loc[region, :] += row

gaez_region = pd.DataFrame(gaez_tropical_humid[1:], columns=gaez_tropical_humid[0]).set_index('Region')
df = pd.DataFrame(columns=gaez_region.columns.copy())
for region in gaez_region.index:
    df.loc[region + ':Excel'] = gaez_region.loc[region, :]
    df.loc[region + ':spatial'] = spatial_region.loc[region, :]
    df.loc[region + ':spatial', 'total'] = df.loc[region + ':spatial'].sum()
df.fillna(0).astype(int).to_csv('results/AEZ-Tropical-Humid.csv')

gaez_region = pd.DataFrame(gaez_temperate_boreal_humid[1:], columns=gaez_temperate_boreal_humid[0]).set_index('Region')
df = pd.DataFrame(columns=gaez_region.columns.copy())
for region in gaez_region.index:
    df.loc[region + ':Excel'] = gaez_region.loc[region, :]
    df.loc[region + ':spatial'] = spatial_region.loc[region, :]
    df.loc[region + ':spatial', 'total'] = df.loc[region + ':spatial'].sum()
df.fillna(0).astype(int).to_csv('results/AEZ-Temperate-Boreal-Humid.csv')

gaez_region = pd.DataFrame(gaez_tropical_semiarid[1:], columns=gaez_tropical_semiarid[0]).set_index('Region')
df = pd.DataFrame(columns=gaez_region.columns.copy())
for region in gaez_region.index:
    df.loc[region + ':Excel'] = gaez_region.loc[region, :]
    df.loc[region + ':spatial'] = spatial_region.loc[region, :]
    df.loc[region + ':spatial', 'total'] = df.loc[region + ':spatial'].sum()
df.fillna(0).astype(int).to_csv('results/AEZ-Tropical-Semiarid.csv')

gaez_region = pd.DataFrame(gaez_temperate_boreal_semiarid[1:], columns=gaez_temperate_boreal_semiarid[0]).set_index('Region')
df = pd.DataFrame(columns=gaez_region.columns.copy())
for region in gaez_region.index:
    df.loc[region + ':Excel'] = gaez_region.loc[region, :]
    df.loc[region + ':spatial'] = spatial_region.loc[region, :]
    df.loc[region + ':spatial', 'total'] = df.loc[region + ':spatial'].sum()
df.fillna(0).astype(int).to_csv('results/AEZ-Tropical-Boreal-Semiarid.csv')

gaez_region = pd.DataFrame(gaez_global_arid[1:], columns=gaez_global_arid[0]).set_index('Region')
df = pd.DataFrame(columns=gaez_region.columns.copy())
for region in gaez_region.index:
    df.loc[region + ':Excel'] = gaez_region.loc[region, :]
    df.loc[region + ':spatial'] = spatial_region.loc[region, :]
    df.loc[region + ':spatial', 'total'] = df.loc[region + ':spatial'].sum()
df.fillna(0).astype(int).to_csv('results/AEZ-Arid.csv')

gaez_region = pd.DataFrame(gaez_global_arctic[1:], columns=gaez_global_arctic[0]).set_index('Region')
df = pd.DataFrame(columns=gaez_region.columns.copy())
for region in gaez_region.index:
    df.loc[region + ':Excel'] = gaez_region.loc[region, :]
    df.loc[region + ':spatial'] = spatial_region.loc[region, :]
    df.loc[region + ':spatial', 'total'] = df.loc[region + ':spatial'].sum()
df.fillna(0).astype(int).to_csv('results/AEZ-Arctic.csv')
