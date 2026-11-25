SELECT 
    p.product_id, 
    COALESCE(ROUND(SUM(p.price * u.units)::numeric / NULLIF(SUM(u.units), 0), 2), 0) AS average_price
FROM prices p 
LEFT JOIN unitsSold u 
    ON p.product_id = u.product_id 
    AND purchase_date BETWEEN start_date AND end_date
GROUP BY p.product_id;