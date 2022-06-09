namespace cs_gui;
using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data.SQLite;
using System.Collections.Generic;

public partial class Party_Panel : Panel {
    public Party_Panel() {
        this.BackColor = SystemColors.Window;
        this.ClientSize = new Size(1000, 700);
        set_box();
    }
    
    // パーツ生成
    GroupBox party01 = new GroupBox() {
        Text = "1体目",
        Size = new Size(350, 185),
        Location = new Point(100, 50)
    };
    GroupBox party02 = new GroupBox() {
        Text = "2体目",
        Size = new Size(350, 185),
        Location = new Point(550, 50)
    };
    GroupBox party03 = new GroupBox() {
        Text = "3体目",
        Size = new Size(350, 185),
        Location = new Point(100, 250)
    };
    GroupBox party04 = new GroupBox() {
        Text = "4体目",
        Size = new Size(350, 185),
        Location = new Point(550, 250)
    };
    GroupBox party05 = new GroupBox() {
        Text = "5体目",
        Size = new Size(350, 185),
        Location = new Point(100, 450)
    };
    GroupBox party06 = new GroupBox() {
        Text = "6体目",
        Size = new Size(350, 185),
        Location = new Point(550, 450)
    };


    Label name_text_01 = new Label() {
        Name = "Name",
        Text = "名前",
        Location = new Point(10, 25),
        Size = new Size(80, 25)
    };
    Label folm_text_01 = new Label() {
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(170, 25),
        Size = new Size(80, 25)
    };
    Label type1_text_01 = new Label(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(10, 50),
        Size = new Size(80, 25)
    };
    Label type2_text_01 = new Label(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(10, 75),
        Size = new Size(80, 25)
    };
    Label abi_text_01 = new Label(){
        Name = "abi",
        Text = "特性",
        Location = new Point(10, 100),
        Size = new Size(80, 25)
    };
    Label char_text_01 = new Label() {
        Name = "char",
        Text = "性格",
        Location = new Point(10, 125),
        Size = new Size(80, 25)
    };
    Label invent_text_01 = new Label() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    Label move1_text_01 = new Label() {
        Name = "move1",
        Text = "技1",
        Location = new Point(170, 50),
        Size = new Size(80, 25)
    };
    Label move2_text_01 = new Label() {
        Name = "move2",
        Text = "技2",
        Location = new Point(170, 75),
        Size = new Size(80, 25)
    };
    Label move3_text_01 = new Label() {
        Name = "move3",
        Text = "技3",
        Location = new Point(170, 100),
        Size = new Size(80, 25)
    };
    Label move4_text_01 = new Label() {
        Name = "move4",
        Text = "技4",
        Location = new Point(170, 125),
        Size = new Size(80, 25)
    };

    ComboBox name_box_01 = new ComboBox(){
        Name = "Name",
        Text = "名前",
        Location = new Point(90, 25),
        Size = new Size(80, 25),
    };
    ComboBox folm_box_01 = new ComboBox(){
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(260, 25),
        Size = new Size(80, 25),
    };
    TextBox type1_box_01 = new TextBox(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(90, 50),
        Size = new Size(80, 25),
    };
    TextBox type2_box_01 = new TextBox(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(90, 75),
        Size = new Size(80, 25)
    };
    TextBox abi_box_01 = new TextBox(){
        Name = "abi",
        Text = "特性",
        Location = new Point(90, 100),
        Size = new Size(80, 25)
    };
    TextBox char_box_01 = new TextBox() {
        Name = "char",
        Text = "性格",
        Location = new Point(90, 125),
        Size = new Size(80, 25)
    };
    TextBox invent_box_01 = new TextBox() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(90, 150),
        Size = new Size(80, 25)
    };
    TextBox move1_box_01 = new TextBox() {
        Name = "move1",
        Text = "技1",
        Location = new Point(260, 50),
        Size = new Size(80, 25)
    };
    TextBox move2_box_01 = new TextBox() {
        Name = "move2",
        Text = "技2",
        Location = new Point(260, 75),
        Size = new Size(80, 25)
    };
    TextBox move3_box_01 = new TextBox() {
        Name = "move3",
        Text = "技3",
        Location = new Point(260, 100),
        Size = new Size(80, 25)
    };
    TextBox move4_box_01 = new TextBox() {
        Name = "move4",
        Text = "技4",
        Location = new Point(260, 125),
        Size = new Size(80, 25)
    };
    Label effort_text_01 = new Label() {
        Name = "effort",
        Text = "努力値",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    TextBox effort_box_01 = new TextBox() {
        Name = "effort",
        Text = "努力調整",
        Location = new Point(90, 150),
        Size = new Size(160, 25)
    };

    Label name_text_02 = new Label() {
        Name = "Name",
        Text = "名前",
        Location = new Point(10, 25),
        Size = new Size(80, 25)
    };
    Label folm_text_02 = new Label() {
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(170, 25),
        Size = new Size(80, 25)
    };
    Label type1_text_02 = new Label(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(10, 50),
        Size = new Size(80, 25)
    };
    Label type2_text_02 = new Label(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(10, 75),
        Size = new Size(80, 25)
    };
    Label abi_text_02 = new Label(){
        Name = "abi",
        Text = "特性",
        Location = new Point(10, 100),
        Size = new Size(80, 25)
    };
    Label char_text_02 = new Label() {
        Name = "char",
        Text = "性格",
        Location = new Point(10, 125),
        Size = new Size(80, 25)
    };
    Label invent_text_02 = new Label() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    Label move1_text_02 = new Label() {
        Name = "move1",
        Text = "技1",
        Location = new Point(170, 50),
        Size = new Size(80, 25)
    };
    Label move2_text_02 = new Label() {
        Name = "move2",
        Text = "技2",
        Location = new Point(170, 75),
        Size = new Size(80, 25)
    };
    Label move3_text_02 = new Label() {
        Name = "move3",
        Text = "技3",
        Location = new Point(170, 100),
        Size = new Size(80, 25)
    };
    Label move4_text_02 = new Label() {
        Name = "move4",
        Text = "技4",
        Location = new Point(170, 125),
        Size = new Size(80, 25)
    };

    ComboBox name_box_02 = new ComboBox(){
        Name = "Name",
        Text = "名前",
        Location = new Point(90, 25),
        Size = new Size(80, 25),
    };
    ComboBox folm_box_02 = new ComboBox(){
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(260, 25),
        Size = new Size(80, 25),
    };
    TextBox type1_box_02 = new TextBox(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(90, 50),
        Size = new Size(80, 25),
    };
    TextBox type2_box_02 = new TextBox(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(90, 75),
        Size = new Size(80, 25)
    };
    TextBox abi_box_02 = new TextBox(){
        Name = "abi",
        Text = "特性",
        Location = new Point(90, 100),
        Size = new Size(80, 25)
    };
    TextBox char_box_02 = new TextBox() {
        Name = "char",
        Text = "性格",
        Location = new Point(90, 125),
        Size = new Size(80, 25)
    };
    TextBox invent_box_02 = new TextBox() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(90, 150),
        Size = new Size(80, 25)
    };
    TextBox move1_box_02 = new TextBox() {
        Name = "move1",
        Text = "技1",
        Location = new Point(260, 50),
        Size = new Size(80, 25)
    };
    TextBox move2_box_02 = new TextBox() {
        Name = "move2",
        Text = "技2",
        Location = new Point(260, 75),
        Size = new Size(80, 25)
    };
    TextBox move3_box_02 = new TextBox() {
        Name = "move3",
        Text = "技3",
        Location = new Point(260, 100),
        Size = new Size(80, 25)
    };
    TextBox move4_box_02 = new TextBox() {
        Name = "move4",
        Text = "技4",
        Location = new Point(260, 125),
        Size = new Size(80, 25)
    };
    Label effort_text_02 = new Label() {
        Name = "effort",
        Text = "努力値",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    TextBox effort_box_02 = new TextBox() {
        Name = "effort",
        Text = "努力調整",
        Location = new Point(90, 150),
        Size = new Size(160, 25)
    };

    Label name_text_03 = new Label() {
        Name = "Name",
        Text = "名前",
        Location = new Point(10, 25),
        Size = new Size(80, 25)
    };
    Label folm_text_03 = new Label() {
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(170, 25),
        Size = new Size(80, 25)
    };
    Label type1_text_03 = new Label(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(10, 50),
        Size = new Size(80, 25)
    };
    Label type2_text_03 = new Label(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(10, 75),
        Size = new Size(80, 25)
    };
    Label abi_text_03 = new Label(){
        Name = "abi",
        Text = "特性",
        Location = new Point(10, 100),
        Size = new Size(80, 25)
    };
    Label char_text_03 = new Label() {
        Name = "char",
        Text = "性格",
        Location = new Point(10, 125),
        Size = new Size(80, 25)
    };
    Label invent_text_03 = new Label() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    Label move1_text_03 = new Label() {
        Name = "move1",
        Text = "技1",
        Location = new Point(170, 50),
        Size = new Size(80, 25)
    };
    Label move2_text_03 = new Label() {
        Name = "move2",
        Text = "技2",
        Location = new Point(170, 75),
        Size = new Size(80, 25)
    };
    Label move3_text_03 = new Label() {
        Name = "move3",
        Text = "技3",
        Location = new Point(170, 100),
        Size = new Size(80, 25)
    };
    Label move4_text_03 = new Label() {
        Name = "move4",
        Text = "技4",
        Location = new Point(170, 125),
        Size = new Size(80, 25)
    };

    ComboBox name_box_03 = new ComboBox(){
        Name = "Name",
        Text = "名前",
        Location = new Point(90, 25),
        Size = new Size(80, 25),
    };
    ComboBox folm_box_03 = new ComboBox(){
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(260, 25),
        Size = new Size(80, 25),
    };
    TextBox type1_box_03 = new TextBox(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(90, 50),
        Size = new Size(80, 25),
    };
    TextBox type2_box_03 = new TextBox(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(90, 75),
        Size = new Size(80, 25)
    };
    TextBox abi_box_03 = new TextBox(){
        Name = "abi",
        Text = "特性",
        Location = new Point(90, 100),
        Size = new Size(80, 25)
    };
    TextBox char_box_03 = new TextBox() {
        Name = "char",
        Text = "性格",
        Location = new Point(90, 125),
        Size = new Size(80, 25)
    };
    TextBox invent_box_03 = new TextBox() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(90, 150),
        Size = new Size(80, 25)
    };
    TextBox move1_box_03 = new TextBox() {
        Name = "move1",
        Text = "技1",
        Location = new Point(260, 50),
        Size = new Size(80, 25)
    };
    TextBox move2_box_03 = new TextBox() {
        Name = "move2",
        Text = "技2",
        Location = new Point(260, 75),
        Size = new Size(80, 25)
    };
    TextBox move3_box_03 = new TextBox() {
        Name = "move3",
        Text = "技3",
        Location = new Point(260, 100),
        Size = new Size(80, 25)
    };
    TextBox move4_box_03 = new TextBox() {
        Name = "move4",
        Text = "技4",
        Location = new Point(260, 125),
        Size = new Size(80, 25)
    };
    Label effort_text_03 = new Label() {
        Name = "effort",
        Text = "努力値",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    TextBox effort_box_03 = new TextBox() {
        Name = "effort",
        Text = "努力調整",
        Location = new Point(90, 150),
        Size = new Size(160, 25)
    };

    Label name_text_04 = new Label() {
        Name = "Name",
        Text = "名前",
        Location = new Point(10, 25),
        Size = new Size(80, 25)
    };
    Label folm_text_04 = new Label() {
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(170, 25),
        Size = new Size(80, 25)
    };
    Label type1_text_04 = new Label(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(10, 50),
        Size = new Size(80, 25)
    };
    Label type2_text_04 = new Label(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(10, 75),
        Size = new Size(80, 25)
    };
    Label abi_text_04 = new Label(){
        Name = "abi",
        Text = "特性",
        Location = new Point(10, 100),
        Size = new Size(80, 25)
    };
    Label char_text_04 = new Label() {
        Name = "char",
        Text = "性格",
        Location = new Point(10, 125),
        Size = new Size(80, 25)
    };
    Label invent_text_04 = new Label() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    Label move1_text_04 = new Label() {
        Name = "move1",
        Text = "技1",
        Location = new Point(170, 50),
        Size = new Size(80, 25)
    };
    Label move2_text_04 = new Label() {
        Name = "move2",
        Text = "技2",
        Location = new Point(170, 75),
        Size = new Size(80, 25)
    };
    Label move3_text_04 = new Label() {
        Name = "move3",
        Text = "技3",
        Location = new Point(170, 100),
        Size = new Size(80, 25)
    };
    Label move4_text_04 = new Label() {
        Name = "move4",
        Text = "技4",
        Location = new Point(170, 125),
        Size = new Size(80, 25)
    };

    ComboBox name_box_04 = new ComboBox(){
        Name = "Name",
        Text = "名前",
        Location = new Point(90, 25),
        Size = new Size(80, 25),
    };
    ComboBox folm_box_04 = new ComboBox(){
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(260, 25),
        Size = new Size(80, 25),
    };
    TextBox type1_box_04 = new TextBox(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(90, 50),
        Size = new Size(80, 25),
    };
    TextBox type2_box_04 = new TextBox(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(90, 75),
        Size = new Size(80, 25)
    };
    TextBox abi_box_04 = new TextBox(){
        Name = "abi",
        Text = "特性",
        Location = new Point(90, 100),
        Size = new Size(80, 25)
    };
    TextBox char_box_04 = new TextBox() {
        Name = "char",
        Text = "性格",
        Location = new Point(90, 125),
        Size = new Size(80, 25)
    };
    TextBox invent_box_04 = new TextBox() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(90, 150),
        Size = new Size(80, 25)
    };
    TextBox move1_box_04 = new TextBox() {
        Name = "move1",
        Text = "技1",
        Location = new Point(260, 50),
        Size = new Size(80, 25)
    };
    TextBox move2_box_04 = new TextBox() {
        Name = "move2",
        Text = "技2",
        Location = new Point(260, 75),
        Size = new Size(80, 25)
    };
    TextBox move3_box_04 = new TextBox() {
        Name = "move3",
        Text = "技3",
        Location = new Point(260, 100),
        Size = new Size(80, 25)
    };
    TextBox move4_box_04 = new TextBox() {
        Name = "move4",
        Text = "技4",
        Location = new Point(260, 125),
        Size = new Size(80, 25)
    };
    Label effort_text_04 = new Label() {
        Name = "effort",
        Text = "努力値",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    TextBox effort_box_04 = new TextBox() {
        Name = "effort",
        Text = "努力調整",
        Location = new Point(90, 150),
        Size = new Size(160, 25)
    };

    Label name_text_05 = new Label() {
        Name = "Name",
        Text = "名前",
        Location = new Point(10, 25),
        Size = new Size(80, 25)
    };
    Label folm_text_05 = new Label() {
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(170, 25),
        Size = new Size(80, 25)
    };
    Label type1_text_05 = new Label(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(10, 50),
        Size = new Size(80, 25)
    };
    Label type2_text_05 = new Label(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(10, 75),
        Size = new Size(80, 25)
    };
    Label abi_text_05 = new Label(){
        Name = "abi",
        Text = "特性",
        Location = new Point(10, 100),
        Size = new Size(80, 25)
    };
    Label char_text_05 = new Label() {
        Name = "char",
        Text = "性格",
        Location = new Point(10, 125),
        Size = new Size(80, 25)
    };
    Label invent_text_05 = new Label() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    Label move1_text_05 = new Label() {
        Name = "move1",
        Text = "技1",
        Location = new Point(170, 50),
        Size = new Size(80, 25)
    };
    Label move2_text_05 = new Label() {
        Name = "move2",
        Text = "技2",
        Location = new Point(170, 75),
        Size = new Size(80, 25)
    };
    Label move3_text_05 = new Label() {
        Name = "move3",
        Text = "技3",
        Location = new Point(170, 100),
        Size = new Size(80, 25)
    };
    Label move4_text_05 = new Label() {
        Name = "move4",
        Text = "技4",
        Location = new Point(170, 125),
        Size = new Size(80, 25)
    };

    ComboBox name_box_05 = new ComboBox(){
        Name = "Name",
        Text = "名前",
        Location = new Point(90, 25),
        Size = new Size(80, 25),
    };
    ComboBox folm_box_05 = new ComboBox(){
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(260, 25),
        Size = new Size(80, 25),
    };
    TextBox type1_box_05 = new TextBox(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(90, 50),
        Size = new Size(80, 25),
    };
    TextBox type2_box_05 = new TextBox(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(90, 75),
        Size = new Size(80, 25)
    };
    TextBox abi_box_05 = new TextBox(){
        Name = "abi",
        Text = "特性",
        Location = new Point(90, 100),
        Size = new Size(80, 25)
    };
    TextBox char_box_05 = new TextBox() {
        Name = "char",
        Text = "性格",
        Location = new Point(90, 125),
        Size = new Size(80, 25)
    };
    TextBox invent_box_05 = new TextBox() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(90, 150),
        Size = new Size(80, 25)
    };
    TextBox move1_box_05 = new TextBox() {
        Name = "move1",
        Text = "技1",
        Location = new Point(260, 50),
        Size = new Size(80, 25)
    };
    TextBox move2_box_05 = new TextBox() {
        Name = "move2",
        Text = "技2",
        Location = new Point(260, 75),
        Size = new Size(80, 25)
    };
    TextBox move3_box_05 = new TextBox() {
        Name = "move3",
        Text = "技3",
        Location = new Point(260, 100),
        Size = new Size(80, 25)
    };
    TextBox move4_box_05 = new TextBox() {
        Name = "move4",
        Text = "技4",
        Location = new Point(260, 125),
        Size = new Size(80, 25)
    };
    Label effort_text_05 = new Label() {
        Name = "effort",
        Text = "努力値",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    TextBox effort_box_05 = new TextBox() {
        Name = "effort",
        Text = "努力調整",
        Location = new Point(90, 150),
        Size = new Size(160, 25)
    };

    Label name_text_06 = new Label() {
        Name = "Name",
        Text = "名前",
        Location = new Point(10, 25),
        Size = new Size(80, 25)
    };
    Label folm_text_06 = new Label() {
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(170, 25),
        Size = new Size(80, 25)
    };
    Label type1_text_06 = new Label(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(10, 50),
        Size = new Size(80, 25)
    };
    Label type2_text_06 = new Label(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(10, 75),
        Size = new Size(80, 25)
    };
    Label abi_text_06 = new Label(){
        Name = "abi",
        Text = "特性",
        Location = new Point(10, 100),
        Size = new Size(80, 25)
    };
    Label char_text_06 = new Label() {
        Name = "char",
        Text = "性格",
        Location = new Point(10, 125),
        Size = new Size(80, 25)
    };
    Label invent_text_06 = new Label() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    Label move1_text_06 = new Label() {
        Name = "move1",
        Text = "技1",
        Location = new Point(170, 50),
        Size = new Size(80, 25)
    };
    Label move2_text_06 = new Label() {
        Name = "move2",
        Text = "技2",
        Location = new Point(170, 75),
        Size = new Size(80, 25)
    };
    Label move3_text_06 = new Label() {
        Name = "move3",
        Text = "技3",
        Location = new Point(170, 100),
        Size = new Size(80, 25)
    };
    Label move4_text_06 = new Label() {
        Name = "move4",
        Text = "技4",
        Location = new Point(170, 125),
        Size = new Size(80, 25)
    };

    ComboBox name_box_06 = new ComboBox(){
        Name = "Name",
        Text = "名前",
        Location = new Point(90, 25),
        Size = new Size(80, 25),
    };
    ComboBox folm_box_06 = new ComboBox(){
        Name = "Folm",
        Text = "フォルム",
        Location = new Point(260, 25),
        Size = new Size(80, 25),
    };
    TextBox type1_box_06 = new TextBox(){
        Name = "type1",
        Text = "タイプ1",
        Location = new Point(90, 50),
        Size = new Size(80, 25),
    };
    TextBox type2_box_06 = new TextBox(){
        Name = "type2",
        Text = "タイプ2",
        Location = new Point(90, 75),
        Size = new Size(80, 25)
    };
    TextBox abi_box_06 = new TextBox(){
        Name = "abi",
        Text = "特性",
        Location = new Point(90, 100),
        Size = new Size(80, 25)
    };
    TextBox char_box_06 = new TextBox() {
        Name = "char",
        Text = "性格",
        Location = new Point(90, 125),
        Size = new Size(80, 25)
    };
    TextBox invent_box_06 = new TextBox() {
        Name = "invent",
        Text = "持ち物",
        Location = new Point(90, 150),
        Size = new Size(80, 25)
    };
    TextBox move1_box_06 = new TextBox() {
        Name = "move1",
        Text = "技1",
        Location = new Point(260, 50),
        Size = new Size(80, 25)
    };
    TextBox move2_box_06 = new TextBox() {
        Name = "move2",
        Text = "技2",
        Location = new Point(260, 75),
        Size = new Size(80, 25)
    };
    TextBox move3_box_06 = new TextBox() {
        Name = "move3",
        Text = "技3",
        Location = new Point(260, 100),
        Size = new Size(80, 25)
    };
    TextBox move4_box_06 = new TextBox() {
        Name = "move4",
        Text = "技4",
        Location = new Point(260, 125),
        Size = new Size(80, 25)
    };
    Label effort_text_06 = new Label() {
        Name = "effort",
        Text = "努力値",
        Location = new Point(10, 150),
        Size = new Size(80, 25)
    };
    TextBox effort_box_06 = new TextBox() {
        Name = "effort",
        Text = "努力調整",
        Location = new Point(90, 150),
        Size = new Size(160, 25)
    };


    public void set_box() {
        party01.Controls.AddRange(new Control[] {
            name_text_01,
            folm_text_01,
            type1_text_01,
            type2_text_01,
            abi_text_01,
            char_text_01,
            move1_text_01,
            move2_text_01,
            move3_text_01,
            move4_text_01,
            effort_text_01,

            name_box_01,
            folm_box_01,
            type1_box_01,
            type2_box_01,
            abi_box_01,
            char_box_01,
            move1_box_01,
            move2_box_01,
            move3_box_01,
            move4_box_01,
            effort_box_01
        });

        party02.Controls.AddRange(new Control[] {
            name_text_02,
            folm_text_02,
            type1_text_02,
            type2_text_02,
            abi_text_02,
            char_text_02,
            move1_text_02,
            move2_text_02,
            move3_text_02,
            move4_text_02,
            effort_text_02,

            name_box_02,
            folm_box_02,
            type1_box_02,
            type2_box_02,
            abi_box_02,
            char_box_02,
            move1_box_02,
            move2_box_02,
            move3_box_02,
            move4_box_02,
            effort_box_02
        });

        party03.Controls.AddRange(new Control[] {
            name_text_03,
            folm_text_03,
            type1_text_03,
            type2_text_03,
            abi_text_03,
            char_text_03,
            move1_text_03,
            move2_text_03,
            move3_text_03,
            move4_text_03,
            effort_text_03,

            name_box_03,
            folm_box_03,
            type1_box_03,
            type2_box_03,
            abi_box_03,
            char_box_03,
            move1_box_03,
            move2_box_03,
            move3_box_03,
            move4_box_03,
            effort_box_03
        });

        party04.Controls.AddRange(new Control[] {
            name_text_04,
            folm_text_04,
            type1_text_04,
            type2_text_04,
            abi_text_04,
            char_text_04,
            move1_text_04,
            move2_text_04,
            move3_text_04,
            move4_text_04,
            effort_text_04,

            name_box_04,
            folm_box_04,
            type1_box_04,
            type2_box_04,
            abi_box_04,
            char_box_04,
            move1_box_04,
            move2_box_04,
            move3_box_04,
            move4_box_04,
            effort_box_04
        });

        party05.Controls.AddRange(new Control[] {
            name_text_05,
            folm_text_05,
            type1_text_05,
            type2_text_05,
            abi_text_05,
            char_text_05,
            move1_text_05,
            move2_text_05,
            move3_text_05,
            move4_text_05,
            effort_text_05,

            name_box_05,
            folm_box_05,
            type1_box_05,
            type2_box_05,
            abi_box_05,
            char_box_05,
            move1_box_05,
            move2_box_05,
            move3_box_05,
            move4_box_05,
            effort_box_05
        });

        party06.Controls.AddRange(new Control[] {
            name_text_06,
            folm_text_06,
            type1_text_06,
            type2_text_06,
            abi_text_06,
            char_text_06,
            move1_text_06,
            move2_text_06,
            move3_text_06,
            move4_text_06,
            effort_text_06,

            name_box_06,
            folm_box_06,
            type1_box_06,
            type2_box_06,
            abi_box_06,
            char_box_06,
            move1_box_06,
            move2_box_06,
            move3_box_06,
            move4_box_06,
            effort_box_06
        });


        this.Controls.AddRange(new Control[] {
            party01,
            party02,
            party03,
            party04,
            party05,
            party06,
        });
    }
    
}
