SELECT owners.*, COUNT(dogs.id) AS dog_count FROM owners
INNER JOIN dogs
ON dogs.owner_id = owners.id
GROUP BY dogs.owner_id
HAVING dog_count > 1
ORDER BY dog_count DESC
LIMIT 1;