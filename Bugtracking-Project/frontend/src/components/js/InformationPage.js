import React from 'react';
import '../css/InformationPage.css'; // Import custom CSS for the information page

const InformationPage = () => {
  return (
    <div className="info-page">
      <h1 className="info-title">What is a Local Bug Tracker (LBT)?</h1>
      <p className="info-description">
        A Local Bug Tracker (LBT) is a system designed to help developers track and manage bugs in a software project. 
        With an LBT, you can:
      </p>
      <ul className="info-list">
        <li>Report bugs found during the development process.</li>
        <li>Assign bugs to team members for resolution.</li>
        <li>Track the status of bugs as they are fixed or closed.</li>
      </ul>
      <p className="info-description">A well-maintained bug tracker helps improve the overall quality and stability of the software project.</p>
    </div>
  );
};

export default InformationPage;
