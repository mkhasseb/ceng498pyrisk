/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created: Sun May 15 18:57:51 2011
**      by: Qt User Interface Compiler version 4.6.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGraphicsView>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QListWidget>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPlainTextEdit>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGraphicsView *mapView;
    QPushButton *passButton;
    QLabel *label_3;
    QLabel *stateLabel;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLineEdit *connectInput;
    QPushButton *connectButton;
    QLabel *playerLabel;
    QGraphicsView *playerView;
    QLabel *missionLabel;
    QWidget *layoutWidget1;
    QVBoxLayout *verticalLayout;
    QLabel *label_2;
    QPlainTextEdit *gameLog;
    QWidget *layoutWidget2;
    QVBoxLayout *verticalLayout_5;
    QLabel *label_5;
    QListWidget *contList;
    QWidget *widget;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer;
    QPushButton *tradeButton;
    QLabel *label_4;
    QListWidget *cardList;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->setEnabled(true);
        MainWindow->resize(1220, 939);
        MainWindow->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #888, stop: 1 #888);\n"
"}\n"
"\n"
"QMainWindow, #centralWidget, QListWidget, QLabel, QPlainTextEdit, QComboBox, QMessageBox, QInputDialog, QPlainTextEdit::handle {\n"
" color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"b"
                        "ackground: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"}\n"
"\n"
"QSpinBox {\n"
" color: #333;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"}\n"
"QGraphicsView, QLineEdit {\n"
"	 color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"\n"
"}"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        centralWidget->setStyleSheet(QString::fromUtf8(""));
        mapView = new QGraphicsView(centralWidget);
        mapView->setObjectName(QString::fromUtf8("mapView"));
        mapView->setGeometry(QRect(20, 250, 761, 501));
        mapView->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);"));
        passButton = new QPushButton(centralWidget);
        passButton->setObjectName(QString::fromUtf8("passButton"));
        passButton->setEnabled(true);
        passButton->setGeometry(QRect(820, 180, 114, 32));
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(20, 180, 751, 51));
        QFont font;
        font.setFamily(QString::fromUtf8("Arial"));
        font.setPointSize(24);
        font.setItalic(true);
        font.setUnderline(true);
        label_3->setFont(font);
        stateLabel = new QLabel(centralWidget);
        stateLabel->setObjectName(QString::fromUtf8("stateLabel"));
        stateLabel->setGeometry(QRect(20, 60, 361, 31));
        layoutWidget = new QWidget(centralWidget);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(20, 10, 369, 35));
        horizontalLayout = new QHBoxLayout(layoutWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(layoutWidget);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        connectInput = new QLineEdit(layoutWidget);
        connectInput->setObjectName(QString::fromUtf8("connectInput"));

        horizontalLayout->addWidget(connectInput);

        connectButton = new QPushButton(layoutWidget);
        connectButton->setObjectName(QString::fromUtf8("connectButton"));
        connectButton->setEnabled(true);
        connectButton->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout->addWidget(connectButton);

        playerLabel = new QLabel(centralWidget);
        playerLabel->setObjectName(QString::fromUtf8("playerLabel"));
        playerLabel->setGeometry(QRect(410, 10, 131, 41));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Arial"));
        font1.setPointSize(20);
        playerLabel->setFont(font1);
        playerView = new QGraphicsView(centralWidget);
        playerView->setObjectName(QString::fromUtf8("playerView"));
        playerView->setGeometry(QRect(540, 10, 51, 41));
        playerView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        playerView->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        missionLabel = new QLabel(centralWidget);
        missionLabel->setObjectName(QString::fromUtf8("missionLabel"));
        missionLabel->setGeometry(QRect(400, 60, 361, 71));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Arial"));
        font2.setPointSize(9);
        font2.setItalic(true);
        missionLabel->setFont(font2);
        missionLabel->setLineWidth(1);
        missionLabel->setWordWrap(true);
        layoutWidget1 = new QWidget(centralWidget);
        layoutWidget1->setObjectName(QString::fromUtf8("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(820, 220, 258, 227));
        verticalLayout = new QVBoxLayout(layoutWidget1);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        label_2 = new QLabel(layoutWidget1);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        verticalLayout->addWidget(label_2);

        gameLog = new QPlainTextEdit(layoutWidget1);
        gameLog->setObjectName(QString::fromUtf8("gameLog"));

        verticalLayout->addWidget(gameLog);

        layoutWidget2 = new QWidget(centralWidget);
        layoutWidget2->setObjectName(QString::fromUtf8("layoutWidget2"));
        layoutWidget2->setGeometry(QRect(790, 10, 351, 161));
        verticalLayout_5 = new QVBoxLayout(layoutWidget2);
        verticalLayout_5->setSpacing(6);
        verticalLayout_5->setContentsMargins(11, 11, 11, 11);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        verticalLayout_5->setContentsMargins(0, 0, 0, 0);
        label_5 = new QLabel(layoutWidget2);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        verticalLayout_5->addWidget(label_5);

        contList = new QListWidget(layoutWidget2);
        contList->setObjectName(QString::fromUtf8("contList"));

        verticalLayout_5->addWidget(contList);

        widget = new QWidget(centralWidget);
        widget->setObjectName(QString::fromUtf8("widget"));
        widget->setGeometry(QRect(870, 690, 210, 33));
        horizontalLayout_2 = new QHBoxLayout(widget);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer = new QSpacerItem(108, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        tradeButton = new QPushButton(widget);
        tradeButton->setObjectName(QString::fromUtf8("tradeButton"));
        tradeButton->setEnabled(false);

        horizontalLayout_2->addWidget(tradeButton);

        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(820, 460, 261, 31));
        cardList = new QListWidget(centralWidget);
        cardList->setObjectName(QString::fromUtf8("cardList"));
        cardList->setEnabled(true);
        cardList->setGeometry(QRect(820, 490, 256, 192));
        cardList->setMinimumSize(QSize(256, 192));
        cardList->setSelectionMode(QAbstractItemView::MultiSelection);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1220, 23));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);
        QObject::connect(connectButton, SIGNAL(clicked()), MainWindow, SLOT(connect()));
        QObject::connect(passButton, SIGNAL(clicked()), MainWindow, SLOT(dopass()));
        QObject::connect(MainWindow, SIGNAL(log(QString)), gameLog, SLOT(appendPlainText(QString)));
        QObject::connect(MainWindow, SIGNAL(loadImgSig()), MainWindow, SLOT(loadImgSlt()));
        QObject::connect(MainWindow, SIGNAL(signalDefendPopup(QString)), MainWindow, SLOT(slotDefendPopup(QString)));
        QObject::connect(MainWindow, SIGNAL(signalTransferPopup()), MainWindow, SLOT(slotTransferPopup()));
        QObject::connect(tradeButton, SIGNAL(clicked()), MainWindow, SLOT(slotTradeIn()));
        QObject::connect(MainWindow, SIGNAL(signalPlayerName(QString)), MainWindow, SLOT(slotPlayerName(QString)));
        QObject::connect(MainWindow, SIGNAL(signalMission(QString)), MainWindow, SLOT(slotMission(QString)));
        QObject::connect(MainWindow, SIGNAL(signalVictor(QString)), MainWindow, SLOT(slotVictor(QString)));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        passButton->setText(QApplication::translate("MainWindow", "Pass", 0, QApplication::UnicodeUTF8));
        label_3->setText(QString());
        stateLabel->setText(QApplication::translate("MainWindow", "State:", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "<host>:<port>", 0, QApplication::UnicodeUTF8));
        connectInput->setText(QApplication::translate("MainWindow", "localhost:8080", 0, QApplication::UnicodeUTF8));
        connectButton->setText(QApplication::translate("MainWindow", "Connect", 0, QApplication::UnicodeUTF8));
        playerLabel->setText(QString());
        missionLabel->setText(QApplication::translate("MainWindow", "Mission: ", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "Game Log", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("MainWindow", "Continents", 0, QApplication::UnicodeUTF8));
        tradeButton->setText(QApplication::translate("MainWindow", "Trade In", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("MainWindow", "Cards", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
