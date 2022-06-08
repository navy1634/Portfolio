namespace cs_gui;
using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data.SQLite;
using System.Collections.Generic;

public partial class Move_Panel : Panel {
    public Move_Panel() {
        this.BackColor = SystemColors.Window;
        this.ClientSize = new Size(1000, 700);
        set_move_damage_button();
        option_layout();

    }

    #nullable disable
    public void option_layout() {
        // close_button.Click += form_close;

        this.Controls.AddRange(new Control[] {
            reset_button,
            close_button
        });
    }

    // パーツ生成
    private
    ListView pk_move_table = new ListView() {
        View = View.Details,
        GridLines = true,
        Size = new Size(850, 350),
        Location = new Point(75, 280)
    };
    Button reset_button = new Button() {
        Name = "reset",
        Text = "リセット",
        Location = new Point(420, 240),
        Size = new Size(80, 20)
    };
    Button close_button = new Button() {
        Name = "Close",
        Text = "閉じる",
        Location = new Point(500, 240),
        Size = new Size(80, 20)
    };
    
    // ポケモン関係
    Label name_label = new Label() {
        Name = "Name",
        Text = "技名",
        Location = new Point(220, 50),
        Size = new Size(80, 25)
    };
    Label type_label = new Label(){
        Name = "type",
        Text = "タイプ",
        Location = new Point(220, 75),
        Size = new Size(80, 25)
    };
    Label class_label = new Label(){
        Name = "class",
        Text = "分類",
        Location = new Point(220, 100),
        Size = new Size(80, 25)
    };
    Label move_way = new Label() {
        Name = "move_way",
        Text = "攻撃方法",
        Location = new Point(220, 125),
        Size = new Size(80, 25)
    };
    Label move_targ = new Label() {
        Name = "target",
        Text = "攻撃対象",
        Location = new Point(220, 150),
        Size = new Size(80, 25)
    };

    ComboBox name_button = new ComboBox() {
        Name = "Name",
        Text = "技名",
        Location = new Point(300, 50),
        Size = new Size(80, 25)
    };
    ComboBox type_button = new ComboBox(){
        Name = "type",
        Text = "タイプ",
        Location = new Point(300, 75),
        Size = new Size(80, 25)
    };
    ComboBox class_button = new ComboBox(){
        Name = "class",
        Text = "分類",
        Location = new Point(300, 100),
        Size = new Size(80, 25)
    };
    ComboBox move_way_button = new ComboBox() {
        Name = "move_way",
        Text = "攻撃方法",
        Location = new Point(300, 125),
        Size = new Size(80, 25)
    };
    ComboBox move_targ_button = new ComboBox() {
        Name = "target",
        Text = "攻撃対象",
        Location = new Point(300, 150),
        Size = new Size(80, 25)
    };

    Label move_damage_upper = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 50),
        Size = new Size(80, 25)
    };
    Label move_big_damage_upper = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 75),
        Size = new Size(80, 25)
    };
    Label move_pp_upper = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 100),
        Size = new Size(80, 25)
    };
    Label move_hitrate_upper = new Label(){
        Name = "以上",
        Text = "以上",
        Location = new Point(540, 125),
        Size = new Size(80, 25)
    };
    Label move_damage_lower = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 50),
        Size = new Size(80, 25)
    };
    Label move_big_damage_lower = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 75),
        Size = new Size(80, 25)
    };
    Label move_pp_lower = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 100),
        Size = new Size(80, 25)
    };
    Label move_hitrate_lower = new Label(){
        Name = "以下",
        Text = "以下",
        Location = new Point(700, 125),
        Size = new Size(80, 25)
    };

    Label move_damage_text= new Label(){
        Name = "damage",
        Text = "合計値",
        Location = new Point(380, 50),
        Size = new Size(80, 25),
    };
    Label move_big_damage_text = new Label(){
        Name = "big_damage",
        Text = "ダイマックス時",
        Location = new Point(380, 75),
        Size = new Size(80, 25),
    };
    Label move_pp_text = new Label(){
        Name = "pp",
        Text = "PP",
        Location = new Point(380, 100),
        Size = new Size(80, 25),
    };
    Label move_hitrate_text = new Label(){
        Name = "hitrate",
        Text = "命中率",
        Location = new Point(380, 125),
        Size = new Size(80, 25),
    };

    TextBox move_damage_m = new TextBox(){
        Name = "damage",
        Text = "0",
        Location = new Point(460, 50),
        Size = new Size(80, 25),
    };
    TextBox move_big_damage_m = new TextBox(){
        Name = "big_damage",
        Text = "0",
        Location = new Point(460, 75),
        Size = new Size(80, 25),
    };
    TextBox move_pp_m = new TextBox(){
        Name = "A",
        Text = "0",
        Location = new Point(460, 100),
        Size = new Size(80, 25),
    };
    TextBox move_hitrate_m = new TextBox(){
        Name = "hitrate",
        Text = "0",
        Location = new Point(460, 125),
        Size = new Size(80, 25),
    };
    
    TextBox move_damage_M = new TextBox(){
        Name = "damage",
        Text = "255",
        Location = new Point(620, 50),
        Size = new Size(80, 25),
    };
    TextBox move_big_damage_M = new TextBox(){
        Name = "big_damage",
        Text = "255",
        Location = new Point(620, 75),
        Size = new Size(80, 25),
    };
    TextBox move_pp_M = new TextBox(){
        Name = "pp",
        Text = "50",
        Location = new Point(620, 100),
        Size = new Size(80, 25),
    };
    TextBox move_hitrate_M = new TextBox(){
        Name = "hitrate",
        Text = "255",
        Location = new Point(620, 125),
        Size = new Size(80, 25),
    };

    public void set_move_damage_button () {
        this.Controls.AddRange(new Control[] {
            name_label,
            type_label,
            class_label,
            move_way,
            move_targ,
            name_button,
            type_button,
            class_button,
            move_way_button,
            move_targ_button,
        });

        this.Controls.AddRange(new Control[] {
            move_big_damage_lower,
            move_big_damage_m,
            move_big_damage_M,
            move_big_damage_text,
            move_big_damage_upper,
            move_damage_lower,
            move_damage_M,
            move_damage_m,
            move_damage_text,
            move_damage_upper,
            move_pp_lower,
            move_pp_M,
            move_pp_m,
            move_pp_text,
            move_pp_upper,
            move_hitrate_lower,
            move_hitrate_M,
            move_hitrate_m,
            move_hitrate_text,
            move_hitrate_upper,
        });

        this.Controls.Add(pk_move_table);
    }

    string[] type_name_list = new string[] {"ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"};

    // public void form_close (object sender, EventArgs e) {
    //     this.Close();
    // }
}

