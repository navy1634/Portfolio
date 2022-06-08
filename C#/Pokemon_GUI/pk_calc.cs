namespace cs_gui;
using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data.SQLite;
using System.Collections.Generic;

public partial class Calc_Panel : Panel {
    public Calc_Panel() {
        this.BackColor = SystemColors.Window;
        this.ClientSize = new Size(1000, 700);
        set_box_();
    }
    
    // パーツの作成
    ListView calc_list = new ListView() {
        View = View.Details,
        GridLines = true,
        Size = new Size(800, 100),
        Location = new Point(100, 550)
    };
    Label name_text_my = new Label() {
        Name = "name",
        Text = "名前",
        Size = new Size(80, 25),
        Location = new Point(30, 25)
    };
    Label folm_text_my = new Label() {
        Name = "folm",
        Text = "フォルム",
        Size = new Size(80, 25),
        Location = new Point(30, 50)
    };
    Label level_text_my = new Label() {
        Name = "level",
        Text = "レベル",
        Size = new Size(80, 25),
        Location = new Point(30, 75)
    };
    Label char_text_my = new Label() {
        Name = "char",
        Text = "性格",
        Size = new Size(80, 25),
        Location = new Point(30, 100)
    };
    Label abi_text_my = new Label() {
        Name = "abi",
        Text = "特性",
        Size = new Size(80, 25),
        Location = new Point(30, 125)
    };
    Label invent_text_my = new Label() {
        Name = "invent",
        Text = "持ち物",
        Size = new Size(80, 25),
        Location = new Point(30, 150)
    };
    Label condi_text_my = new Label() {
        Name = "condition",
        Text = "状態異常",
        Size = new Size(80, 25),
        Location = new Point(30, 175)
    };
    Label big_text_my = new Label() {
        Name = "big",
        Text = "ダイマックス時",
        Size = new Size(80, 25),
        Location = new Point(30, 200)
    };

    ComboBox name_box_my = new ComboBox() {
        Name = "name",
        Text = "名前",
        Size = new Size(80, 25),
        Location = new Point(110, 25)
    };
    ComboBox folm_box_my = new ComboBox() {
        Name = "folm",
        Text = "フォルム",
        Size = new Size(80, 25),
        Location = new Point(110, 50)
    };
    ComboBox level_box_my = new ComboBox() {
        Name = "level",
        Text = "レベル",
        Size = new Size(80, 25),
        Location = new Point(110, 75)
    };
    ComboBox char_box_my = new ComboBox() {
        Name = "char",
        Text = "性格",
        Size = new Size(80, 25),
        Location = new Point(110, 100)
    };
    ComboBox abi_box_my = new ComboBox() {
        Name = "abi",
        Text = "特性",
        Size = new Size(80, 25),
        Location = new Point(110, 125)
    };
    ComboBox invent_box_my = new ComboBox() {
        Name = "invent",
        Text = "持ち物",
        Size = new Size(80, 25),
        Location = new Point(110, 150)
    };
    ComboBox condi_box_my = new ComboBox() {
        Name = "condition",
        Text = "状態異常",
        Size = new Size(80, 25),
        Location = new Point(110, 175)
    };
    ComboBox big_box_my = new ComboBox() {
        Name = "big",
        Text = "ダイマックス時",
        Size = new Size(80, 25),
        Location = new Point(110, 200)
    };

    Label status_SUM_text_my = new Label() {
        Name = "sum",
        Text = "合計値",
        Size = new Size(80, 25),
        Location = new Point(190, 200)
    };
    Label status_H_text_my = new Label() {
        Name = "HP",
        Text = "HP",
        Size = new Size(80, 25),
        Location = new Point(190, 50)
    };
    Label status_A_text_my = new Label() {
        Name = "A",
        Text = "攻撃",
        Size = new Size(80, 25),
        Location = new Point(190, 75)
    };
    Label status_B_text_my = new Label() {
        Name = "B",
        Text = "防御",
        Size = new Size(80, 25),
        Location = new Point(190, 100)
    };
    Label status_C_text_my = new Label() {
        Name = "C",
        Text = "特攻",
        Size = new Size(80, 25),
        Location = new Point(190, 125)
    };
    Label status_D_text_my = new Label() {
        Name = "D",
        Text = "特防",
        Size = new Size(80, 25),
        Location = new Point(190, 150)
    };
    Label status_S_text_my = new Label() {
        Name = "S",
        Text = "素早さ",
        Size = new Size(80, 25),
        Location = new Point(190, 175)
    };

    Label status_race_text_my = new Label() {
        Name = "race",
        Text = "種族値",
        Size = new Size(80, 25),
        Location = new Point(270, 25)
    };
    TextBox status_SUM_race_my = new TextBox() {
        Name = "sum",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 200)
    };
    TextBox status_H_race_my = new TextBox() {
        Name = "HP",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 50)
    };
    TextBox status_A_race_my = new TextBox() {
        Name = "A",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 75)
    };
    TextBox status_B_race_my = new TextBox() {
        Name = "B",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 100)
    };
    TextBox status_C_race_my = new TextBox() {
        Name = "C",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 125)
    };
    TextBox status_D_race_my = new TextBox() {
        Name = "D",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 150)
    };
    TextBox status_S_race_my = new TextBox() {
        Name = "S",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 175)
    };

    Label status_effort__text_my = new Label() {
        Name = "effort",
        Text = "努力値",
        Size = new Size(80, 25),
        Location = new Point(350, 25)
    };
    TextBox status_SUM_effort_my = new TextBox() {
        Name = "sum",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(350, 200)
    };
    NumericUpDown status_H_effort_my = new NumericUpDown() {
        Name = "HP",
        Text = "0",
        Maximum = 255,
        Minimum = 0,
        Increment = 4,
        AutoSize = true,
        Size = new Size(80, 25),
        Location = new Point(350, 50)
    };
    NumericUpDown status_A_effort_my = new NumericUpDown() {
        Name = "A",
        Text = "0",
        Maximum = 255,
        Minimum = 0,
        Increment = 4,
        Size = new Size(80, 25),
        Location = new Point(350, 75)
    };
    NumericUpDown status_B_effort_my = new NumericUpDown() {
        Name = "B",
        Text = "0",
        Maximum = 255,
        Minimum = 0,
        Increment = 4,
        Size = new Size(80, 25),
        Location = new Point(350, 100)
    };
    NumericUpDown status_C_effort_my = new NumericUpDown() {
        Name = "C",
        Text = "0",
        Maximum = 255,
        Minimum = 0,
        Increment = 4,
        Size = new Size(80, 25),
        
        Location = new Point(350, 125)
    };
    NumericUpDown status_D_effort_my = new NumericUpDown() {
        Name = "D",
        Text = "0",
        Maximum = 255,
        Minimum = 0,
        Increment = 4,
        Size = new Size(80, 25),
        Location = new Point(350, 150)
    };
    NumericUpDown status_S_effort_my = new NumericUpDown() {
        Name = "S",
        Text = "0",
        Maximum = 255,
        Minimum = 0,
        Increment = 4,
        Size = new Size(80, 25),
        Location = new Point(350, 175)
    };

    Label status_indivi_text_my = new Label() {
        Name = "indivi",
        Text = "個体値",
        Size = new Size(80, 25),
        Location = new Point(430, 25)
    };
    NumericUpDown status_H_indivi_my = new NumericUpDown() {
        Name = "HP",
        Text = "31",
        Maximum = 31,
        Minimum = 0,
        Size = new Size(80, 25),
        Location = new Point(430, 50)
    };
    NumericUpDown status_A_indivi_my = new NumericUpDown() {
        Name = "A",
        Text = "31",
        Maximum = 31,
        Minimum = 0,
        Size = new Size(80, 25),
        Location = new Point(430, 75)
    };
    NumericUpDown status_B_indivi_my = new NumericUpDown() {
        Name = "B",
        Text = "31",
        Maximum = 31,
        Minimum = 0,
        Size = new Size(80, 25),
        Location = new Point(430, 100)
    };
    NumericUpDown status_C_indivi_my = new NumericUpDown() {
        Name = "C",
        Text = "31",
        Maximum = 31,
        Minimum = 0,
        Size = new Size(80, 25),
        Location = new Point(430, 125)
    };
    NumericUpDown status_D_indivi_my = new NumericUpDown() {
        Name = "D",
        Text = "31",
        Maximum = 31,
        Minimum = 0,
        Size = new Size(80, 25),
        Location = new Point(430, 150)
    };
    NumericUpDown status_S_indivi_my = new NumericUpDown() {
        Name = "S",
        Text = "31",
        Maximum = 31,
        Minimum = 0,
        Size = new Size(80, 25),
        Location = new Point(430, 175)
    };

    Label status_rank_text_my = new Label() {
        Name = "rank",
        Text = "ランク",
        Size = new Size(80, 25),
        Location = new Point(510, 25)
    };
    Label status_H_rank_my = new Label() {
        Name = "HP",
        Text = "-",
        Size = new Size(80, 25),
        Location = new Point(510, 50)
    };
    NumericUpDown status_A_rank_my = new NumericUpDown() {
        Name = "A",
        Text = "0",
        Maximum = 31,
        Minimum = 0,
        Size = new Size(80, 25),
        Location = new Point(510, 75)
    };
    NumericUpDown status_B_rank_my = new NumericUpDown() {
        Name = "B",
        Text = "0",
        Maximum = 6,
        Minimum = -6,
        Size = new Size(80, 25),
        Location = new Point(510, 100)
    };
    NumericUpDown status_C_rank_my = new NumericUpDown() {
        Name = "C",
        Text = "0",
        Maximum = 6,
        Minimum = -6,
        Size = new Size(80, 25),
        Location = new Point(510, 125)
    };
    NumericUpDown status_D_rank_my = new NumericUpDown() {
        Name = "D",
        Text = "0",
        Maximum = 6,
        Minimum = -6,
        Size = new Size(80, 25),
        Location = new Point(510, 150)
    };
    NumericUpDown status_S_rank_my = new NumericUpDown() {
        Name = "S",
        Text = "0",
        Maximum = 6,
        Minimum = -6,
        Size = new Size(80, 25),
        Location = new Point(510, 175)
    };

    Label status_real_text_my = new Label() {
        Name = "real",
        Text = "実数値",
        Size = new Size(80, 25),
        Location = new Point(670, 25)
    };
    TextBox status_H_real_my = new TextBox() {
        Name = "HP",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 50)
    };
    TextBox status_A_real_my = new TextBox() {
        Name = "A",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 75)
    };
    TextBox status_B_real_my = new TextBox() {
        Name = "B",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 100)
    };
    TextBox status_C_real_my = new TextBox() {
        Name = "C",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 125)
    };
    TextBox status_D_real_my = new TextBox() {
        Name = "D",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 150)
    };
    TextBox status_S_real_my = new TextBox() {
        Name = "S",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 175)
    };

    Label status_real_correct_text_my = new Label() {
        Name = "real_correct",
        Text = "補正込み実数値",
        Size = new Size(90, 25),
        Location = new Point(750, 25)
    };
    TextBox status_H_real_correct_my = new TextBox() {
        Name = "HP",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 50)
    };
    TextBox status_A_real_correct_my = new TextBox() {
        Name = "A",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 75)
    };
    TextBox status_B_real_correct_my = new TextBox() {
        Name = "B",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 100)
    };
    TextBox status_C_real_correct_my = new TextBox() {
        Name = "C",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 125)
    };
    TextBox status_D_real_correct_my = new TextBox() {
        Name = "D",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 150)
    };
    TextBox status_S_real_correct_my = new TextBox() {
        Name = "S",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 175)
    };

    Label name_text_enem = new Label() {
        Name = "name",
        Text = "名前",
        Size = new Size(80, 25),
        Location = new Point(30, 25)
    };
    Label folm_text_enem = new Label() {
        Name = "folm",
        Text = "フォルム",
        Size = new Size(80, 25),
        Location = new Point(30, 50)
    };
    Label level_text_enem = new Label() {
        Name = "level",
        Text = "レベル",
        Size = new Size(80, 25),
        Location = new Point(30, 75)
    };
    Label char_text_enem = new Label() {
        Name = "char",
        Text = "性格",
        Size = new Size(80, 25),
        Location = new Point(30, 100)
    };
    Label abi_text_enem = new Label() {
        Name = "abi",
        Text = "特性",
        Size = new Size(80, 25),
        Location = new Point(30, 125)
    };
    Label invent_text_enem = new Label() {
        Name = "invent",
        Text = "持ち物",
        Size = new Size(80, 25),
        Location = new Point(30, 150)
    };
    Label condi_text_enem = new Label() {
        Name = "condition",
        Text = "状態異常",
        Size = new Size(80, 25),
        Location = new Point(30, 175)
    };
    Label big_text_enem = new Label() {
        Name = "ex",
        Text = "その他",
        Size = new Size(80, 25),
        Location = new Point(30, 200)
    };

    ComboBox name_box_enem = new ComboBox() {
        Name = "name",
        Text = "名前",
        Size = new Size(80, 25),
        Location = new Point(110, 25)
    };
    ComboBox folm_box_enem = new ComboBox() {
        Name = "folm",
        Text = "フォルム",
        Size = new Size(80, 25),
        Location = new Point(110, 50)
    };
    ComboBox level_box_enem = new ComboBox() {
        Name = "level",
        Text = "レベル",
        Size = new Size(80, 25),
        Location = new Point(110, 75)
    };
    ComboBox char_box_enem = new ComboBox() {
        Name = "char",
        Text = "性格",
        Size = new Size(80, 25),
        Location = new Point(110, 100)
    };
    ComboBox abi_box_enem = new ComboBox() {
        Name = "abi",
        Text = "特性",
        Size = new Size(80, 25),
        Location = new Point(110, 125)
    };
    ComboBox invent_box_enem = new ComboBox() {
        Name = "invent",
        Text = "持ち物",
        Size = new Size(80, 25),
        Location = new Point(110, 150)
    };
    ComboBox condi_box_enem = new ComboBox() {
        Name = "condition",
        Text = "状態異常",
        Size = new Size(80, 25),
        Location = new Point(110, 175)
    };
    ComboBox big_box_enem = new ComboBox() {
        Name = "ex",
        Text = "その他",
        Size = new Size(80, 25),
        Location = new Point(110, 200)
    };

    Label status_SUM_text_enem = new Label() {
        Name = "sum",
        Text = "合計値",
        Size = new Size(80, 25),
        Location = new Point(190, 200)
    };
    Label status_H_text_enem = new Label() {
        Name = "HP",
        Text = "HP",
        Size = new Size(80, 25),
        Location = new Point(190, 50)
    };
    Label status_A_text_enem = new Label() {
        Name = "A",
        Text = "攻撃",
        Size = new Size(80, 25),
        Location = new Point(190, 75)
    };
    Label status_B_text_enem = new Label() {
        Name = "B",
        Text = "防御",
        Size = new Size(80, 25),
        Location = new Point(190, 100)
    };
    Label status_C_text_enem = new Label() {
        Name = "C",
        Text = "特攻",
        Size = new Size(80, 25),
        Location = new Point(190, 125)
    };
    Label status_D_text_enem = new Label() {
        Name = "D",
        Text = "特防",
        Size = new Size(80, 25),
        Location = new Point(190, 150)
    };
    Label status_S_text_enem = new Label() {
        Name = "S",
        Text = "素早さ",
        Size = new Size(80, 25),
        Location = new Point(190, 175)
    };

    Label status_race_text_enem = new Label() {
        Name = "race",
        Text = "種族値",
        Size = new Size(80, 25),
        Location = new Point(270, 25)
    };
    TextBox status_SUM_race_enem = new TextBox() {
        Name = "sum",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 200)
    };
    TextBox status_H_race_enem = new TextBox() {
        Name = "HP",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 50)
    };
    TextBox status_A_race_enem = new TextBox() {
        Name = "A",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 75)
    };
    TextBox status_B_race_enem = new TextBox() {
        Name = "B",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 100)
    };
    TextBox status_C_race_enem = new TextBox() {
        Name = "C",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 125)
    };
    TextBox status_D_race_enem = new TextBox() {
        Name = "D",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 150)
    };
    TextBox status_S_race_enem = new TextBox() {
        Name = "S",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(270, 175)
    };

    Label status_effort__text_enem = new Label() {
        Name = "effort",
        Text = "努力値",
        Size = new Size(80, 25),
        Location = new Point(350, 25)
    };
    TextBox status_SUM_effort_enem = new TextBox() {
        Name = "sum",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(350, 200)
    };
    TextBox status_H_effort_enem = new TextBox() {
        Name = "HP",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(350, 50)
    };
    TextBox status_A_effort_enem = new TextBox() {
        Name = "A",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(350, 75)
    };
    TextBox status_B_effort_enem = new TextBox() {
        Name = "B",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(350, 100)
    };
    TextBox status_C_effort_enem = new TextBox() {
        Name = "C",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(350, 125)
    };
    TextBox status_D_effort_enem = new TextBox() {
        Name = "D",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(350, 150)
    };
    TextBox status_S_effort_enem = new TextBox() {
        Name = "S",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(350, 175)
    };

    Label status_indivi_text_enem = new Label() {
        Name = "indivi",
        Text = "個体値",
        Size = new Size(80, 25),
        Location = new Point(430, 25)
    };
    TextBox status_H_indivi_enem = new TextBox() {
        Name = "HP",
        Text = "31",
        Size = new Size(80, 25),
        Location = new Point(430, 50)
    };
    TextBox status_A_indivi_enem = new TextBox() {
        Name = "A",
        Text = "31",
        Size = new Size(80, 25),
        Location = new Point(430, 75)
    };
    TextBox status_B_indivi_enem = new TextBox() {
        Name = "B",
        Text = "31",
        Size = new Size(80, 25),
        Location = new Point(430, 100)
    };
    TextBox status_C_indivi_enem = new TextBox() {
        Name = "C",
        Text = "31",
        Size = new Size(80, 25),
        Location = new Point(430, 125)
    };
    TextBox status_D_indivi_enem = new TextBox() {
        Name = "D",
        Text = "31",
        Size = new Size(80, 25),
        Location = new Point(430, 150)
    };
    TextBox status_S_indivi_enem = new TextBox() {
        Name = "S",
        Text = "31",
        Size = new Size(80, 25),
        Location = new Point(430, 175)
    };

    Label status_rank_text_enem = new Label() {
        Name = "rank",
        Text = "ランク",
        Size = new Size(80, 25),
        Location = new Point(510, 25)
    };
    Label status_H_rank_enem = new Label() {
        Name = "HP",
        Text = "-",
        Size = new Size(80, 25),
        Location = new Point(510, 50)
    };
    TextBox status_A_rank_enem = new TextBox() {
        Name = "A",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(510, 75)
    };
    TextBox status_B_rank_enem = new TextBox() {
        Name = "B",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(510, 100)
    };
    TextBox status_C_rank_enem = new TextBox() {
        Name = "C",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(510, 125)
    };
    TextBox status_D_rank_enem = new TextBox() {
        Name = "D",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(510, 150)
    };
    TextBox status_S_rank_enem = new TextBox() {
        Name = "S",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(510, 175)
    };

    Label status_real_text_enem = new Label() {
        Name = "real",
        Text = "実数値",
        Size = new Size(80, 25),
        Location = new Point(670, 25)
    };
    TextBox status_H_real_enem = new TextBox() {
        Name = "HP",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 50)
    };
    TextBox status_A_real_enem = new TextBox() {
        Name = "A",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 75)
    };
    TextBox status_B_real_enem = new TextBox() {
        Name = "B",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 100)
    };
    TextBox status_C_real_enem = new TextBox() {
        Name = "C",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 125)
    };
    TextBox status_D_real_enem = new TextBox() {
        Name = "D",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 150)
    };
    TextBox status_S_real_enem = new TextBox() {
        Name = "S",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(670, 175)
    };

    Label status_real_correct_text_enem = new Label() {
        Name = "real_correct",
        Text = "補正込み実数値",
        Size = new Size(90, 25),
        Location = new Point(750, 25)
    };
    TextBox status_H_real_correct_enem = new TextBox() {
        Name = "HP",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 50)
    };
    TextBox status_A_real_correct_enem = new TextBox() {
        Name = "A",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 75)
    };
    TextBox status_B_real_correct_enem = new TextBox() {
        Name = "B",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 100)
    };
    TextBox status_C_real_correct_enem = new TextBox() {
        Name = "C",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 125)
    };
    TextBox status_D_real_correct_enem = new TextBox() {
        Name = "D",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 150)
    };
    TextBox status_S_real_correct_enem = new TextBox() {
        Name = "S",
        Text = "0",
        Size = new Size(80, 25),
        Location = new Point(750, 175)
    };

    GroupBox group_my = new GroupBox() {
        Text = "攻撃側",
        Size = new Size(860, 238),
        Location = new Point(70, 12)
    };
    GroupBox group_enem = new GroupBox() {
        Text = "防御側",
        Size = new Size(860, 238),
        Location = new Point(70, 262)
    };
    
    public void set_box_() {
        group_my.Controls.AddRange(new Control[] {
            name_text_my,
            folm_text_my,
            level_text_my,
            char_text_my,
            abi_text_my,
            invent_text_my,
            condi_text_my,
            big_text_my,
            name_box_my,
            folm_box_my,
            level_box_my,
            char_box_my,
            abi_box_my,
            invent_box_my,
            condi_box_my,
            big_box_my,
            status_race_text_my,
            status_effort__text_my,
            status_indivi_text_my,
            status_rank_text_my,
            status_real_text_my,
            status_real_correct_text_my,
        });
        group_my.Controls.AddRange(new Control[] {
            status_SUM_text_my,
            status_SUM_race_my,
            status_SUM_effort_my,
            status_H_text_my,
            status_H_race_my,
            status_H_effort_my,
            status_H_indivi_my,
            status_H_rank_my,
            status_H_real_my,
            status_H_real_correct_my,
            status_A_text_my,
            status_A_race_my,
            status_A_effort_my,
            status_A_indivi_my,
            status_A_rank_my,
            status_A_real_my,
            status_A_real_correct_my,
            status_B_text_my,
            status_B_race_my,
            status_B_effort_my,
            status_B_indivi_my,
            status_B_rank_my,
            status_B_real_my,
            status_B_real_correct_my,
            status_C_text_my,
            status_C_race_my,
            status_C_effort_my,
            status_C_indivi_my,
            status_C_rank_my,
            status_C_real_my,
            status_C_real_correct_my,
            status_D_text_my,
            status_D_race_my,
            status_D_effort_my,
            status_D_indivi_my,
            status_D_rank_my,
            status_D_real_my,
            status_D_real_correct_my,
            status_S_text_my,
            status_S_race_my,
            status_S_effort_my,
            status_S_indivi_my,
            status_S_rank_my,
            status_S_real_my,
            status_S_real_correct_my,
        });
        group_enem.Controls.AddRange(new Control[] {
            name_text_enem,
            folm_text_enem,
            level_text_enem,
            char_text_enem,
            abi_text_enem,
            invent_text_enem,
            condi_text_enem,
            big_text_enem,
            name_box_enem,
            folm_box_enem,
            level_box_enem,
            char_box_enem,
            abi_box_enem,
            invent_box_enem,
            condi_box_enem,
            big_box_enem,
            status_race_text_enem,
            status_effort__text_enem,
            status_indivi_text_enem,
            status_rank_text_enem,
            status_real_text_enem,
            status_real_correct_text_enem,
        });
        group_enem.Controls.AddRange(new Control[] {
            status_SUM_text_enem,
            status_SUM_race_enem,
            status_SUM_effort_enem,
            status_H_text_enem,
            status_H_race_enem,
            status_H_effort_enem,
            status_H_indivi_enem,
            status_H_rank_enem,
            status_H_real_enem,
            status_H_real_correct_enem,
            status_A_text_enem,
            status_A_race_enem,
            status_A_effort_enem,
            status_A_indivi_enem,
            status_A_rank_enem,
            status_A_real_enem,
            status_A_real_correct_enem,
            status_B_text_enem,
            status_B_race_enem,
            status_B_effort_enem,
            status_B_indivi_enem,
            status_B_rank_enem,
            status_B_real_enem,
            status_B_real_correct_enem,
            status_C_text_enem,
            status_C_race_enem,
            status_C_effort_enem,
            status_C_indivi_enem,
            status_C_rank_enem,
            status_C_real_enem,
            status_C_real_correct_enem,
            status_D_text_enem,
            status_D_race_enem,
            status_D_effort_enem,
            status_D_indivi_enem,
            status_D_rank_enem,
            status_D_real_enem,
            status_D_real_correct_enem,
            status_S_text_enem,
            status_S_race_enem,
            status_S_effort_enem,
            status_S_indivi_enem,
            status_S_rank_enem,
            status_S_real_enem,
            status_S_real_correct_enem,
        });
        this.Controls.Add(calc_list);
        this.Controls.AddRange(new Control[] {
            group_my, group_enem
        });
    }
}
