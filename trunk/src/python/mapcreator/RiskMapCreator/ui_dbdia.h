/********************************************************************************
** Form generated from reading UI file 'dbdia.ui'
**
** Created: Mon Apr 25 16:35:08 2011
**      by: Qt User Interface Compiler version 4.6.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DBDIA_H
#define UI_DBDIA_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout_5;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QLineEdit *username;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_2;
    QLineEdit *fullname;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_3;
    QLineEdit *password;
    QVBoxLayout *verticalLayout;
    QSpacerItem *verticalSpacer_2;
    QPushButton *insertButton;
    QSpacerItem *verticalSpacer;
    QLabel *status;
    QHBoxLayout *horizontalLayout;
    QLineEdit *searchEdit;
    QPushButton *searchButton;
    QPushButton *pushButton;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(400, 219);
        verticalLayout_3 = new QVBoxLayout(Dialog);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(Dialog);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        username = new QLineEdit(Dialog);
        username->setObjectName(QString::fromUtf8("username"));

        horizontalLayout_2->addWidget(username);


        verticalLayout_2->addLayout(horizontalLayout_2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_2 = new QLabel(Dialog);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_3->addWidget(label_2);

        fullname = new QLineEdit(Dialog);
        fullname->setObjectName(QString::fromUtf8("fullname"));

        horizontalLayout_3->addWidget(fullname);


        verticalLayout_2->addLayout(horizontalLayout_3);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        label_3 = new QLabel(Dialog);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_4->addWidget(label_3);

        password = new QLineEdit(Dialog);
        password->setObjectName(QString::fromUtf8("password"));
        password->setEchoMode(QLineEdit::Password);

        horizontalLayout_4->addWidget(password);


        verticalLayout_2->addLayout(horizontalLayout_4);


        horizontalLayout_5->addLayout(verticalLayout_2);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_2);

        insertButton = new QPushButton(Dialog);
        insertButton->setObjectName(QString::fromUtf8("insertButton"));

        verticalLayout->addWidget(insertButton);


        horizontalLayout_5->addLayout(verticalLayout);


        verticalLayout_3->addLayout(horizontalLayout_5);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_3->addItem(verticalSpacer);

        status = new QLabel(Dialog);
        status->setObjectName(QString::fromUtf8("status"));

        verticalLayout_3->addWidget(status);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        searchEdit = new QLineEdit(Dialog);
        searchEdit->setObjectName(QString::fromUtf8("searchEdit"));

        horizontalLayout->addWidget(searchEdit);

        searchButton = new QPushButton(Dialog);
        searchButton->setObjectName(QString::fromUtf8("searchButton"));

        horizontalLayout->addWidget(searchButton);


        verticalLayout_3->addLayout(horizontalLayout);

        pushButton = new QPushButton(Dialog);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        verticalLayout_3->addWidget(pushButton);


        retranslateUi(Dialog);
        QObject::connect(pushButton, SIGNAL(clicked()), Dialog, SLOT(accept()));
        QObject::connect(searchButton, SIGNAL(clicked()), Dialog, SLOT(searchitem()));
        QObject::connect(insertButton, SIGNAL(clicked(bool)), Dialog, SLOT(insertitem()));

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("Dialog", "username", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("Dialog", "Full name", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("Dialog", "Password", 0, QApplication::UnicodeUTF8));
        insertButton->setText(QApplication::translate("Dialog", "Insert", 0, QApplication::UnicodeUTF8));
        status->setText(QApplication::translate("Dialog", "TextLabel", 0, QApplication::UnicodeUTF8));
        searchButton->setText(QApplication::translate("Dialog", "Search", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("Dialog", "Exit", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DBDIA_H
