namespace cs_gui;
using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data.SQLite;

public partial class Move_Panel : Panel {
    public Move_Panel() {
        this.BackColor = SystemColors.Window;
        this.ClientSize = new Size(1000, 700);
        set_move_damage_button();
        set_move_table();
        option_layout();
        get_Start_SQL();
    }

    #nullable disable
    private void Search_SQL(object sender, EventArgs e) {
        using (var conn = new SQLiteConnection("Data Source=./GUI/use_data/py_db.db")){
            using (var command = conn.CreateCommand()) {
                // 接続
                conn.Open();

                // コマンドの実行処理
                command.CommandText =  Create_Query();
                using (SQLiteDataReader reader = command.ExecuteReader()) {
                    while (reader.Read()) {
                        pk_move_table.Items.Add(new ListViewItem(new string[] {
                            reader.GetValue(0).ToString(),
                            reader.GetValue(1).ToString(),
                            reader.GetValue(2).ToString(),
                            reader.GetValue(3).ToString(),
                            reader.GetValue(4).ToString(),
                            reader.GetValue(5).ToString(),
                            reader.GetValue(6).ToString(),
                            reader.GetValue(7).ToString(),
                            reader.GetValue(8).ToString(),
                            reader.GetValue(9).ToString(),
                            reader.GetValue(10).ToString(),
                        }));
                    }
                }
            }
        }
    }
    private void get_Start_SQL() {
        using (var conn = new SQLiteConnection("Data Source=./GUI/use_data/py_db.db")){
            using (var command = conn.CreateCommand()) {
                // 接続
                conn.Open();

                // コマンドの実行処理
                command.CommandText =  Create_Query();
                using (SQLiteDataReader reader = command.ExecuteReader()) {
                    while (reader.Read()) {
                        pk_move_table.Items.Add(new ListViewItem(new string[] {
                            reader.GetValue(0).ToString(),
                            reader.GetValue(1).ToString(),
                            reader.GetValue(2).ToString(),
                            reader.GetValue(3).ToString(),
                            reader.GetValue(4).ToString(),
                            reader.GetValue(5).ToString(),
                            reader.GetValue(6).ToString(),
                            reader.GetValue(7).ToString(),
                            reader.GetValue(8).ToString(),
                            reader.GetValue(9).ToString(),
                            reader.GetValue(10).ToString(),
                        }));
                    }
                }
            }
        }
    }

    public string Create_Query() {
        string query = @"Select * From pk_move";
        if (move_name.Text != "技名") {
            query += String.Format($" and pk_move.技名 Like '%{move_name.Text}%'");
        }
        if (move_type.Text != "タイプ") {
            query += String.Format($" and pk_move.タイプ == '{move_type.Text}'");
        }
        if (move_class.Text != "分類") {
            query += String.Format($" and pk_move.分類 == '{move_class.Text}'");
        }
        if (move_way.Text != "攻撃方法") {
            query += String.Format($" and pk_move.攻撃方法 == '{move_way.Text}'");
        }
        if (move_target.Text != "対象") {
            query += String.Format($" and pk_move.攻撃対象 == '{move_target.Text}'");
        }
        return query;
    }

    // パーツ生成
    ListView pk_move_table = new ListView() {
        View = View.Details,
        GridLines = true,
        Size = new Size(850, 350),
        Location = new Point(75, 280)
    };

    ColumnHeader move_name;
    ColumnHeader move_type;
    ColumnHeader move_class;
    ColumnHeader move_power;
    ColumnHeader move_big;
    ColumnHeader move_hit;
    ColumnHeader move_pp;
    ColumnHeader move_way;
    ColumnHeader move_protect;
    ColumnHeader move_target;
    ColumnHeader move_effect;

    public void set_move_table() {
        move_name = new ColumnHeader() {
            Text = "技名",
            Width = 80
        };
        move_type = new ColumnHeader() {
            Text = "タイプ",
            Width = 80
        };
        move_class = new ColumnHeader() {
            Text = "分類",
            Width = 80
        };
        move_power = new ColumnHeader() {
            Text = "威力",
            Width = 80
        };
        move_big = new ColumnHeader() {
            Text = "ダイマックス時",
            Width = 80
        };
        move_hit = new ColumnHeader() {
            Text = "命中率",
            Width = 80
        };
        move_pp = new ColumnHeader() {
            Text = "PP",
            Width = 80
        };
        move_way = new ColumnHeader() {
            Text = "攻撃方法",
            Width = 80
        };
        move_protect = new ColumnHeader() {
            Text = "守る",
            Width = 80
        };
        move_target = new ColumnHeader() {
            Text = "対象",
            Width = 80
        };
        move_effect = new ColumnHeader() {
            Text = "効果",
            Width = 140
        };
        pk_move_table.Columns.AddRange(new ColumnHeader[] {
            move_name,
            move_type,
            move_class,
            move_power,
            move_big,
            move_hit,
            move_pp,
            move_way,
            move_protect,
            move_target,
            move_effect
        });
    }

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
    Label move_way_label = new Label() {
        Name = "move_way",
        Text = "攻撃方法",
        Location = new Point(220, 125),
        Size = new Size(80, 25)
    };
    Label move_targ_label = new Label() {
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

    public void option_layout() {
        this.Controls.AddRange(new Control[] {
            reset_button,
            close_button
        });
        reset_button.Click += reset_box;
    }

    public void set_move_damage_button () {
        name_button.Items.Add("技名");
        name_button.Click += Search_SQL;
        type_button.Items.AddRange(type_name_list);
        type_button.Click += Search_SQL;
        class_button.Items.AddRange(move_class_list);
        class_button.Click += Search_SQL;
        move_way_button.Items.AddRange(new string[] {"攻撃方法", "接触", "非接触"});
        move_way_button.Click += Search_SQL;
        move_targ_button.Items.AddRange(type_name_list);
        move_targ_button.Click += Search_SQL;

        this.Controls.AddRange(new Control[] {
            name_label,
            type_label,
            class_label,
            move_way_label,
            move_targ_label,
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

    public void reset_box(object sender, EventArgs e) {
        name_button.Text = "技名";
        type_button.Text = "タイプ";
        class_button.Text = "分類";
        move_way_button.Text = "攻撃方法";
        move_targ_button.Text = "攻撃対象";
    }

    string[] type_name_list = new string[] {"タイプ", "ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"};
    string[] move_class_list = new string[] {"分類", "物理", "特殊", "変化", "Z技", "ダイマックス"};
    string[] move_target_list = new string[] {"対象", "自分", "味方1体", "相手1体", "自分か味方", "味方全体", "相手全体", "全体", "ランダム1体", "自分以外", "味方の場", "相手の場", "全体の場", "不定"};
}
