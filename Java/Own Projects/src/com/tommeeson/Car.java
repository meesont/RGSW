package com.tommeeson;

import java.util.Date;

/**
 * Code within this class is property of Mee8a
 * Using the code without permission is copyright infringement
 * Please contact Mee8a on spigot if you wish to use the code.
 */

public class Car {

    String registration, make;
    int milage;
    Date inspectionDate;

    public Car(String registration, String make, int milage, Date inspectionDate) {
        this.registration = registration;
        this.make = make;
        this.milage = milage;
        this.inspectionDate = inspectionDate;
    }

    public Date getInspectionDate() {
        return inspectionDate;
    }

    public int getMilage() {
        return milage;
    }

    public String getMake() {
        return make;
    }

    public String getRegistration() {
        return registration;
    }

    public void setInspectionDate(Date inspectionDate) {
        this.inspectionDate = inspectionDate;
    }

    public void setMilage(int milage) {
        this.milage = milage;
    }
}
