# Получение списка логинов курьеров с количеством их заказов в статусе "В доставке""
SELECT c.login, 
    COUNT(o.id) AS "deliveryCount" 
FROM "Couriers" AS c 
LEFT JOIN "Orders" AS o ON c.id = o."courierId" 
WHERE o."inDelivery" = true 
GROUP BY c.login;

# Получить все трекеры заказов и их статусы. 
# Статусы определяются по следующему правилу:
#   Если поле finished == true, то вывести статус 2.
#   Если поле canсelled == true, то вывести статус -1.
#   Если поле inDelivery == true, то вывести статус 1.
#   Для остальных случаев вывести 0.
SELECT track, 
    CASE 
        WHEN finished = true THEN 2 
        WHEN cancelled = true THEN -1 
        WHEN "inDelivery" = true THEN 1 
        ELSE 0 
    END AS state 
FROM "Orders";
