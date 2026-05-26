from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from healthcalc.gender import Gender
from healthcalc.unit_system import UnitSystem
from healthcalc.language import Language


@dataclass
class HealthData:
    weight: Optional[float] = None
    height: Optional[float] = None
    gender: Optional[Gender] = None
    waist: Optional[float] = None
    hip: Optional[float] = None
    unit_system: UnitSystem = UnitSystem.METRIC
    language: Language = Language.ENGLISH

    def normalize(self) -> "HealthData":
        unit_system = self.unit_system

        return HealthData(
            weight=self._normalize_weight(unit_system),
            height=self._normalize_height(unit_system),
            gender=self.gender,
            waist=self._normalize_length(unit_system, self.waist),
            hip=self._normalize_length(unit_system, self.hip),
            unit_system=UnitSystem.METRIC,
            language=self.language,
        )

    def _normalize_weight(self, unit_system: UnitSystem) -> Optional[float]:
        if self.weight is None:
            return None

        if unit_system == UnitSystem.GRAMS:
            return self.weight / 1000.0

        if unit_system == UnitSystem.LBS:
            return self.weight * 0.453592

        return self.weight

    def _normalize_height(self, unit_system: UnitSystem) -> Optional[float]:
        if self.height is None:
            return None

        if unit_system == UnitSystem.INCHES:
            return self.height * 0.0254

        return self.height

    def _normalize_length(self, unit_system: UnitSystem, value: Optional[float]) -> Optional[float]:
        if value is None:
            return None

        if unit_system == UnitSystem.INCHES:
            return value * 0.0254

        return value


    @staticmethod
    def kg_to_lbs(weight_kg: float) -> float:
        return weight_kg * 2.20462

    @staticmethod
    def lbs_to_kg(weight_lbs: float) -> float:
        return weight_lbs * 0.453592

    @staticmethod
    def kg_to_grams(weight_kg: float) -> float:
        return weight_kg * 1000.0

    @staticmethod
    def grams_to_kg(weight_grams: float) -> float:
        return weight_grams / 1000.0

    @staticmethod
    def inches_to_m(length_inch: float) -> float:
        return length_inch * 0.0254

    @staticmethod
    def m_to_inches(length_m: float) -> float:
        return length_m * 39.3701
