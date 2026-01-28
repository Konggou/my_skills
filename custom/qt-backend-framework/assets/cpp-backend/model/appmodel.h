#ifndef APPMODEL_H
#define APPMODEL_H

#include <QString>

/**
 * Generic data model for backend layer.
 * Hold domain data; no Qt signals required unless you need change notification.
 */
class AppModel
{
public:
    AppModel() = default;

    QString status() const { return m_status; }
    void setStatus(const QString &s) { m_status = s; }

private:
    QString m_status;
};

#endif // APPMODEL_H
