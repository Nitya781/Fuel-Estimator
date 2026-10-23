"""
=========================================================
Specific Fuel Consumption (SFC) Model
---------------------------------------------------------
Computes engine Specific Fuel Consumption using a
parametric model.

SFC = Base SFC
      × Mach Correction
      × Temperature Correction
      × Throttle Correction

Author : HAL Fuel Estimation Project
=========================================================
"""

from models.atmosphere_model import AtmosphereModel


class SFCModel:
    """
    Computes Specific Fuel Consumption (TSFC).

    Units:
        Output : lb / lbf / hr
    """

    def __init__(
        self,
        dry_sfc: float,
        afterburner_sfc: float
    ):
        """
        Parameters
        ----------
        dry_sfc : float
            Base SFC during dry thrust.

        afterburner_sfc : float
            Base SFC during afterburner.
        """

        self.dry_sfc = dry_sfc
        self.afterburner_sfc = afterburner_sfc

        self.atmosphere = AtmosphereModel()

    def calculate(
        self,
        mach: float,
        throttle: float,
        ambient_temperature_degC: float,
        afterburner: bool
    ) -> float:
        """
        Calculate Specific Fuel Consumption.

        Parameters
        ----------
        mach : float

        throttle : float
            Range : 0.0 - 1.0

        ambient_temperature_degC : float

        afterburner : bool

        Returns
        -------
        float
            SFC (lb/lbf/hr)
        """

        # -------------------------------------------------
        # Base SFC
        # -------------------------------------------------

        if afterburner:
            base_sfc = self.afterburner_sfc
        else:
            base_sfc = self.dry_sfc

        # -------------------------------------------------
        # Convert Celsius to Kelvin
        # -------------------------------------------------

        temperature_K = ambient_temperature_degC + 273.15

        # -------------------------------------------------
        # Atmospheric Temperature Ratio
        # -------------------------------------------------

        temperature_factor = self.atmosphere.temperature_ratio(
            temperature_K
        )

        # -------------------------------------------------
        # Mach Correction
        # -------------------------------------------------

        mach_factor = (
            1.0 +
            (0.15 * (mach ** 2))
        )

        # -------------------------------------------------
        # Throttle Correction
        # -------------------------------------------------

        throttle_factor = (
            1.0 +
            (0.5 * ((1.0 - throttle) ** 2))
        )

        # -------------------------------------------------
        # Final SFC
        # -------------------------------------------------

        sfc = (
            base_sfc
            * mach_factor
            * temperature_factor
            * throttle_factor
        )

        return sfc
