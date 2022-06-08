namespace cs_gui;
using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data.SQLite;
using System.Collections.Generic;

public partial class Data_Panel : Panel {
    public Data_Panel() {
        this.BackColor = SystemColors.Window;
        this.ClientSize = new Size(1000, 700);
        set_status_button();
        option_status_layout();
    }

    #nullable disable
    public void set_box() {
    }


    public void option_status_layout() {
        // close_button.Click += form_close;

        this.Controls.AddRange(new Control[] {
            move_gene,
            close_button,
        });
    }
    // パーツ生成
    private
    pk_damage_table type_table = new pk_damage_table() {
        View = View.Details,
        GridLines = true,
        Size = new Size(380, 195),
        Location = new Point(75, 355)
    };
    pk_move_table move_table = new pk_move_table() {
        View = View.Details,
        GridLines = true,
        Size = new Size(380, 500),
        Location = new Point(520, 75)
    };

    ComboBox move_gene = new ComboBox() {
        Name = "move",
        Text = "世代",
        Location = new Point(210, 295),
        Size = new Size(80, 25)
    };
    Button close_button = new Button() {
        Name = "Close",
        Text = "閉じる",
        Location = new Point(290, 295),
        Size = new Size(80, 25)
    };
    
    // ポケモン関係
    Label name_label = new Label() {
        Name = "Name",
        Text = "名前",
        Location = new Point(130, 75),
        Size = new Size(80, 25)
    };
    Label folm_label = new Label() {
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(300, 75),
        Size = new Size(80, 25)
    };
    Label type1_label = new Label(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(130, 100),
        Size = new Size(80, 25)
    };
    Label type2_label = new Label(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(130, 125),
        Size = new Size(80, 25)
    };
    Label abi1_label = new Label(){
        Name = "abi1",
        Text = "特性1",
        Location = new Point(130, 150),
        Size = new Size(80, 25)
    };
    Label abi2_label = new Label(){
        Name = "abi2",
        Text = "特性2",
        Location = new Point(130, 175),
        Size = new Size(80, 25)
    };
    Label abi_hide_label = new Label(){
        Name = "abi",
        Text = "隠れ特性",
        Location = new Point(130, 200),
        Size = new Size(80, 25)
    };
    Label gene_label = new Label(){
        Name = "gene",
        Text = "世代",
        Location = new Point(130, 225),
        Size = new Size(80, 25)
    };
    Label class_label = new Label(){
        Name = "class",
        Text = "分類",
        Location = new Point(130, 250),
        Size = new Size(80, 25)
    };

    ComboBox name_button = new ComboBox(){
        Name = "Name",
        Text = "名前",
        Location = new Point(210, 75),
        Size = new Size(80, 25),
    };
    ComboBox folm_button = new ComboBox(){
        // Name = "Folm",
        Text = "フォルム",
        Location = new Point(380, 75),
        Size = new Size(80, 25),
    };
    TextBox type1_button = new TextBox(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(210, 100),
        Size = new Size(80, 25),
    };
    TextBox type2_button = new TextBox(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(210, 125),
        Size = new Size(80, 25)
    };
    TextBox abi1_button = new TextBox(){
        Name = "abi1",
        Text = "特性1",
        Location = new Point(210, 150),
        Size = new Size(80, 25)
    };
    TextBox abi2_button = new TextBox(){
        Name = "abi2",
        Text = "特性2",
        Location = new Point(210, 175),
        Size = new Size(80, 25)
    };
    TextBox abi_hide_button = new TextBox(){
        Name = "abi",
        Text = "隠れ特性",
        Location = new Point(210, 200),
        Size = new Size(80, 25)
    };
    TextBox gene_button = new TextBox(){
        Name = "gene",
        Text = "世代",
        Location = new Point(210, 225),
        Size = new Size(80, 25)
    };
    TextBox class_button = new TextBox(){
        Name = "class",
        Text = "分類",
        Location = new Point(210, 250),
        Size = new Size(80, 25)
    };

    Label status_text_SUM = new Label(){
        Name = "sum",
        Text = "合計値",
        Location = new Point(300, 100),
        Size = new Size(80, 25)
    };
    Label status_text_H = new Label(){
        Name = "H",
        Text = "HP",
        Location = new Point(300, 125),
        Size = new Size(80, 25)
    };
    Label status_text_A = new Label(){
        Name = "A",
        Text = "攻撃",
        Location = new Point(300, 150),
        Size = new Size(80, 25)
    };
    Label status_text_B = new Label(){
        Name = "B",
        Text = "防御",
        Location = new Point(300, 175),
        Size = new Size(80, 25)
    };
    Label status_text_C = new Label(){
        Name = "C",
        Text = "特攻",
        Location = new Point(300, 200),
        Size = new Size(80, 25)
    };
    Label status_text_D = new Label(){
        Name = "D",
        Text = "特防",
        Location = new Point(300, 225),
        Size = new Size(80, 25)
    };
    Label status_text_S = new Label(){
        Name = "S",
        Text = "素早さ",
        Location = new Point(300, 250),
        Size = new Size(80, 25)
    };
    TextBox status_SUM = new TextBox(){
        Name = "sum",
        Text = "合計値",
        Location = new Point(380, 100),
        Size = new Size(80, 25)
    };
    TextBox status_H = new TextBox(){
        Name = "H",
        Text = "HP",
        Location = new Point(380, 125),
        Size = new Size(80, 25)
    };
    TextBox status_A = new TextBox(){
        Name = "A",
        Text = "攻撃",
        Location = new Point(380, 150),
        Size = new Size(80, 25)
    };
    TextBox status_B = new TextBox(){
        Name = "B",
        Text = "防御",
        Location = new Point(380, 175),
        Size = new Size(80, 25)
    };
    TextBox status_C = new TextBox(){
        Name = "C",
        Text = "特攻",
        Location = new Point(380, 200),
        Size = new Size(80, 25)
    };
    TextBox status_D = new TextBox(){
        Name = "D",
        Text = "特防",
        Location = new Point(380, 225),
        Size = new Size(80, 25)
    };
    TextBox status_S = new TextBox(){
        Name = "S",
        Text = "素早さ",
        Location = new Point(380, 250),
        Size = new Size(80, 25)
    };

    public void set_status_button () {
        this.Controls.AddRange(new Control[] {
            name_label,
            folm_label,
            type1_label,
            type2_label,
            abi1_label,
            abi2_label,
            abi_hide_label,
            gene_label,
            class_label,
            name_button,
            folm_button,
            type1_button,
            type2_button,
            abi1_button,
            abi2_button,
            abi_hide_button,
            gene_button,
            class_button,
        });

        this.Controls.AddRange(new Control[] {
            status_text_SUM,
            status_text_H,
            status_text_A,
            status_text_B,
            status_text_C,
            status_text_D,
            status_text_S,
            status_SUM,
            status_H,
            status_A,
            status_B,
            status_C,
            status_D,
            status_S,
        });

        this.Controls.Add(type_table);
        this.Controls.Add(move_table);
    }

    private
    Dictionary<string, int> type_name_list = new Dictionary<string, int>() {{"ノーマル", 0},{"ほのお", 1},{"みず", 2},{"でんき", 3},{"くさ", 4},{"こおり", 5},{"かくとう", 6},{"どく", 7},{"じめん", 8},{"ひこう", 9},{"エスパー", 10},{"むし", 11},{"いわ", 12},{"ゴースト", 13},{"ドラゴン", 14},{"あく", 15},{"はがね", 16},{"フェアリー", 17}};
    string[] move_columns = new string[] {"技名", "タイプ", "取得条件", "効果"};
    string[] type_columns = new string[] {"4倍", "2倍", "半減", "1/4減", "無効"};
    int[] swsh = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 72, 73, 77, 78, 79, 80, 81, 82, 83, 90, 91, 92, 93, 94, 95, 98, 99, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 100, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 125, 151, 163, 164, 169, 170, 171, 172, 173, 174, 150, 176, 177, 178, 182, 183, 184, 185, 186, 194, 195, 196, 197, 199, 202, 206, 208, 211, 212, 213, 214, 215, 220, 221, 222, 223, 224, 200, 226, 227, 230, 233, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 225, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 263, 264, 270, 271, 272, 273, 274, 250, 278, 279, 280, 281, 282, 290, 291, 292, 293, 294, 295, 298, 302, 303, 304, 305, 306, 309, 310, 315, 318, 319, 320, 321, 324, 328, 329, 330, 333, 334, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 355, 356, 359, 360, 361, 362, 363, 364, 365, 369, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 403, 404, 405, 406, 407, 415, 416, 420, 421, 422, 423, 425, 426, 427, 428, 434, 435, 436, 437, 438, 439, 440, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 470, 471, 473, 474, 475, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 494, 506, 507, 508, 509, 510, 517, 518, 519, 520, 521, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 582, 583, 584, 587, 588, 589, 590, 591, 592, 593, 595, 596, 597, 598, 599, 600, 601, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 649, 659, 660, 661, 662, 663, 674, 675, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 736, 737, 738, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 776, 777, 778, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898};
    double[,] comp_list = new double[,] {
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1},
        {1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1},
        {1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1},
        {1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1},
        {1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1},
        {1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1},
        {2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5},
        {1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2},
        {1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1},
        {1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1},
        {1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 2, 0.5, 1},
        {1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5},
        {1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1},
        {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0},
        {1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5},
        {1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2},
        {1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1}
    };
    // public void form_close (object sender, EventArgs e) {
    //     this.Close();
    // }
}

class pk_move_table : ListView {
    ColumnHeader move_name;
    ColumnHeader move_type;
    ColumnHeader move_get;
    ColumnHeader move_effect;

    public pk_move_table() {
        move_name = new ColumnHeader() {
            Text = "技名",
            Width = 80
        };
        move_type = new ColumnHeader() {
            Text = "タイプ",
            Width = 80
        };
        move_get = new ColumnHeader() {
            Text = "取得条件",
            Width = 80
        };
        move_effect = new ColumnHeader() {
            Text = "効果",
            Width = 140
        };
        
        this.Columns.AddRange(new ColumnHeader[] {move_name, move_type, move_get, move_effect});
    }
    string pk_query =  @"Select pk_nomal.名前, pk_nomal.フォルム, pk_fight.タイプ1, pk_fight.タイプ2, pk_fight.特性1, pk_fight.特性2, pk_fight.夢特性, pk_status.合計値, pk_status.H, pk_status.A, pk_status.B, pk_status.C, pk_status.D, pk_status.S, pk_nomal.世代, pk_nomal.分類
            From pk_status, pk_nomal, pk_fight
            Where pk_status.名前 = pk_nomal.名前 and pk_status.フォルム = pk_nomal.フォルム and pk_status.名前 = pk_nomal.名前
            and pk_status.名前 = pk_fight.名前 and pk_status.フォルム = pk_fight.フォルム and pk_status.名前 = pk_fight.名前";

    public void AddColumns() {
        SQLiteConnection conn = new SQLiteConnection();
        conn.ConnectionString = "Data Source=usedata/py_db.db;Version=3;";
        conn.Open();
        SQLiteCommand command = conn.CreateCommand();
        command.CommandText = pk_query;

        var reader = command.ExecuteReader();
        while (reader.Read()) {
            this.Items.Add(new ListViewItem(new string[] {
                reader.GetString(0),
                reader.GetString(1),
                reader.GetString(2),
                reader.GetString(3),
            }));
        }
        conn.Close();
    }
}

class pk_damage_table : ListView {
    ColumnHeader damage_4;
    ColumnHeader damage_2;
    ColumnHeader damage_0;
    ColumnHeader damage_05;
    ColumnHeader damage_025;

    public pk_damage_table() {
        damage_4 = new ColumnHeader() {
            Text = "4倍",
            Width = 76
        };
        damage_2 = new ColumnHeader() {
            Text = "2倍",
            Width = 76
        };
        damage_05 = new ColumnHeader() {
            Text = "半減",
            Width = 76
        };
        damage_025 = new ColumnHeader() {
            Text = "1/4減",
            Width = 76
        };
        damage_0 = new ColumnHeader() {
            Text = "無効",
            Width = 76
        };
        
        this.Columns.AddRange(new ColumnHeader[] { damage_4, damage_2, damage_05, damage_025, damage_0 });
    }
    public void AddColumns(string[] pk_type, Dictionary<string, int> type_name_list, double[,] comp_list) {
        Dictionary<double, List<string>> type_items = calc_type(pk_type, type_name_list, comp_list);
    
        for (int i=0; i<type_items[4].Count; i++) {
            this.Items.Add(new ListViewItem(new string[] {
                type_items[4][i],
                type_items[2][i],
                type_items[0.5][i],
                type_items[0.25][i],
                type_items[0][i]
            }));
        }
    }

    public Dictionary<double, List<string>> calc_type(string[] pk_type, Dictionary<string, int> type_name_list, double[,] comp_list) {
        List<string> damage_4 = new List<string>();
        List<string> damage_2 = new List<string>();
        List<string> damage_0 = new List<string>();
        List<string> damage_05 = new List<string>();
        List<string> damage_025 = new List<string>();
        int type1;
        int type2;
        int move_type_int;
        double rate;

        foreach (string move_type in type_name_list.Keys) {
            move_type_int = type_name_list[move_type];
            type1 = type_name_list[pk_type[0]];

            if (pk_type.Length==2) {
                type2 = type_name_list[pk_type[1]];
                rate = comp_list[move_type_int, type1] * comp_list[move_type_int, type2];
            } else {
                rate = comp_list[move_type_int, type1];
            }

            switch (rate) {
                case 4:
                damage_4.Add(move_type);
                break;
                case 2:
                damage_2.Add(move_type);
                break;
                case 0.5:
                damage_05.Add(move_type);
                break;
                case 0.25:
                damage_025.Add(move_type);
                break;
                case 0:
                damage_0.Add(move_type);
                break;

                default:
                break;
            }
        }
        int[] items_len = {damage_4.Count, damage_2.Count, damage_05.Count, damage_025.Count, damage_0.Count};
        int max_len = items_len.Max();
        while (damage_4.Count==max_len && damage_2.Count==max_len && damage_05.Count==max_len && damage_025.Count==max_len && damage_0.Count==max_len) {
            if (damage_4.Count < max_len) {
                damage_4.Add(" ");
            }
            if (damage_2.Count < max_len) {
                damage_2.Add(" ");
            }
            if (damage_05.Count < max_len) {
                damage_05.Add(" ");
            }
            if (damage_025.Count < max_len) {
                damage_025.Add(" ");
            }
            if (damage_0.Count < max_len) {
                damage_0.Add(" ");
            }
        }

        Dictionary<double, List<string>> damage_comp = new Dictionary<double, List<string>>() {
            {4, damage_4}, {2, damage_2}, {0.5, damage_05}, {0.25, damage_025}, {0, damage_0}
        };
        return damage_comp;
    }
}

