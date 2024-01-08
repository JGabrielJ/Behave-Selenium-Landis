Feature: Register student data
  As a user
  I want to be able to register my student data
  So I can know how they are being stored

  Scenario: Complete and submit the form with the correct data
    Given that I'm on the Registration Form page
    When I complete the form with the correct data
    And I click Submit
    Then I see a pop-up with filled data

  Scenario: Complete and submit the form with incorrect data
    Given that I'm on the Registration Form page
    When I complete the form with incorrect data
    And I click Submit
    Then I see fields in red demanding to be filled out

  Scenario: Do not complete nothing and submit
    Given that I'm on the Registration Form page
    When I click Submit
    Then I see fields in red demanding to be filled out

  Scenario: Remove a single item from Subjects
    Given that I'm on the Registration Form page
    When I remove a single item present in Subjects
    Then I see the whole page blank

  Scenario: Delete the content from Date of Birth
    Given that I'm on the Registration Form page
    When I leave the Date of Birth field empty
    Then I see the whole page blank
