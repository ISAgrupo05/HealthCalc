from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class HealthData:
    weight: Optional[float] = None
    height: Optional[float] = None
    sex: Optional[str] = None
    waist: Optional[float] = None
    hip: Optional[float] = None
    unit_system: str = "METRIC"
    language: str = "EN"

    def normalize(self) -> "HealthData":
        unit_system = self.unit_system.upper()

        return HealthData(
            weight=self._normalize_weight(unit_system),
            height=self._normalize_height(unit_system),
            sex=self._normalize_sex(),
            waist=self._normalize_length(unit_system, self.waist),
            hip=self._normalize_length(unit_system, self.hip),
            unit_system="METRIC",
            language=self.language,
        )

    def _normalize_weight(self, unit_system: str) -> Optional[float]:
        if self.weight is None:
            return None

        if unit_system in {"GRAMS", "G"}:
            return self.weight / 1000.0

        if unit_system in {"LBS", "LB", "POUNDS", "POUND"}:
            return self.weight * 0.453592

        return self.weight

    def _normalize_height(self, unit_system: str) -> Optional[float]:
        if self.height is None:
            return None

        if unit_system in {"INCHES", "IN", "INCH"}:
            return self.height * 0.0254

        return self.height

    def _normalize_length(self, unit_system: str, value: Optional[float]) -> Optional[float]:
        if value is None:
            return None

        if unit_system in {"INCHES", "IN", "INCH"}:
            return value * 0.0254

        return value

    def _normalize_sex(self) -> Optional[str]:
        if self.sex is None:
            return None
        return self.sex.upper()

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
