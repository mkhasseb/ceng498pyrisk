/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created: Mon Apr 25 16:35:08 2011
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
#include <QtGui/QMainWindow>
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QPlainTextEdit>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QStatusBar>
#include <QtGui/QTabWidget>
#include <QtGui/QToolBar>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionOpen;
    QAction *actionSave;
    QWidget *centralWidget;
    QTabWidget *tabWidget;
    QWidget *widget;
    QPlainTextEdit *logText;
    QGraphicsView *mapView;
    QLabel *label;
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label_2;
    QLineEdit *regionName;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *beginButton;
    QPushButton *endButton;
    QHBoxLayout *horizontalLayout_3;
    QSpacerItem *horizontalSpacer;
    QPushButton *clearButton;
    QHBoxLayout *horizontalLayout_4;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *linkButton;
    QWidget *tab_2;
    QMenuBar *menuBar;
    QMenu *menuFile;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1521, 730);
        actionOpen = new QAction(MainWindow);
        actionOpen->setObjectName(QString::fromUtf8("actionOpen"));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QString::fromUtf8("actionSave"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        QSizePolicy sizePolicy(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(centralWidget->sizePolicy().hasHeightForWidth());
        centralWidget->setSizePolicy(sizePolicy);
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setGeometry(QRect(10, 0, 1471, 701));
        widget = new QWidget();
        widget->setObjectName(QString::fromUtf8("widget"));
        sizePolicy.setHeightForWidth(widget->sizePolicy().hasHeightForWidth());
        widget->setSizePolicy(sizePolicy);
        logText = new QPlainTextEdit(widget);
        logText->setObjectName(QString::fromUtf8("logText"));
        logText->setGeometry(QRect(1040, 290, 411, 321));
        mapView = new QGraphicsView(widget);
        mapView->setObjectName(QString::fromUtf8("mapView"));
        mapView->setGeometry(QRect(0, 0, 1001, 611));
        mapView->viewport()->setProperty("cursor", QVariant(QCursor(Qt::CrossCursor)));
        mapView->setMouseTracking(true);
        label = new QLabel(widget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(12, 2, 61, 16));
        layoutWidget = new QWidget(widget);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(1170, 10, 236, 152));
        verticalLayout = new QVBoxLayout(layoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setSizeConstraint(QLayout::SetMinimumSize);
        label_2 = new QLabel(layoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setMaximumSize(QSize(100, 40));

        horizontalLayout->addWidget(label_2);

        regionName = new QLineEdit(layoutWidget);
        regionName->setObjectName(QString::fromUtf8("regionName"));
        QSizePolicy sizePolicy1(QSizePolicy::MinimumExpanding, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(regionName->sizePolicy().hasHeightForWidth());
        regionName->setSizePolicy(sizePolicy1);
        regionName->setMaximumSize(QSize(200, 40));

        horizontalLayout->addWidget(regionName);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setSizeConstraint(QLayout::SetMinimumSize);
        beginButton = new QPushButton(layoutWidget);
        beginButton->setObjectName(QString::fromUtf8("beginButton"));
        sizePolicy1.setHeightForWidth(beginButton->sizePolicy().hasHeightForWidth());
        beginButton->setSizePolicy(sizePolicy1);

        horizontalLayout_2->addWidget(beginButton);

        endButton = new QPushButton(layoutWidget);
        endButton->setObjectName(QString::fromUtf8("endButton"));
        sizePolicy1.setHeightForWidth(endButton->sizePolicy().hasHeightForWidth());
        endButton->setSizePolicy(sizePolicy1);

        horizontalLayout_2->addWidget(endButton);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalLayout_3->setSizeConstraint(QLayout::SetMinimumSize);
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer);

        clearButton = new QPushButton(layoutWidget);
        clearButton->setObjectName(QString::fromUtf8("clearButton"));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(clearButton->sizePolicy().hasHeightForWidth());
        clearButton->setSizePolicy(sizePolicy2);
        clearButton->setMinimumSize(QSize(100, 0));

        horizontalLayout_3->addWidget(clearButton);


        verticalLayout->addLayout(horizontalLayout_3);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_2);

        linkButton = new QPushButton(layoutWidget);
        linkButton->setObjectName(QString::fromUtf8("linkButton"));

        horizontalLayout_4->addWidget(linkButton);


        verticalLayout->addLayout(horizontalLayout_4);

        tabWidget->addTab(widget, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        tabWidget->addTab(tab_2, QString());
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1521, 22));
        menuFile = new QMenu(menuBar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuFile->menuAction());
        menuFile->addAction(actionOpen);
        menuFile->addAction(actionSave);

        retranslateUi(MainWindow);
        QObject::connect(beginButton, SIGNAL(clicked()), MainWindow, SLOT(beginRegion()));
        QObject::connect(endButton, SIGNAL(clicked()), MainWindow, SLOT(endRegion()));
        QObject::connect(clearButton, SIGNAL(clicked()), MainWindow, SLOT(clearRegion()));
        QObject::connect(actionOpen, SIGNAL(triggered()), MainWindow, SLOT(actionOpen()));
        QObject::connect(actionSave, SIGNAL(triggered()), MainWindow, SLOT(actionSave()));
        QObject::connect(linkButton, SIGNAL(clicked()), MainWindow, SLOT(link()));

        tabWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        actionOpen->setText(QApplication::translate("MainWindow", "Open", 0, QApplication::UnicodeUTF8));
        actionSave->setText(QApplication::translate("MainWindow", "Save", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "Map View", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "RegionName", 0, QApplication::UnicodeUTF8));
        beginButton->setText(QApplication::translate("MainWindow", "Begin Area", 0, QApplication::UnicodeUTF8));
        endButton->setText(QApplication::translate("MainWindow", "End Area", 0, QApplication::UnicodeUTF8));
        clearButton->setText(QApplication::translate("MainWindow", "Clear", 0, QApplication::UnicodeUTF8));
        linkButton->setText(QApplication::translate("MainWindow", "Link", 0, QApplication::UnicodeUTF8));
        tabWidget->setTabText(tabWidget->indexOf(widget), QApplication::translate("MainWindow", "Tab 1", 0, QApplication::UnicodeUTF8));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("MainWindow", "Tab 2", 0, QApplication::UnicodeUTF8));
        menuFile->setTitle(QApplication::translate("MainWindow", "File", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
