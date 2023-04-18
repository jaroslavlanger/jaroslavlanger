module RightDivision ((///)) where

infixr  7 ///
(///) :: Fractional a => a -> a -> a
a /// b = a / b
